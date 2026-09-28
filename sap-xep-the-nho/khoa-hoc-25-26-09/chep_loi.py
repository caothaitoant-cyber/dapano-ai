"""Chep loi (speech-to-text) toan bo video DJI trong thu muc khoa hoc.

- Quet de quy thu muc nguon, lay cac file DJI_*.MP4
- Chep loi tieng Viet bang faster-whisper, moi video 1 file .txt (co moc thoi gian)
- File da chep roi se duoc bo qua => chay lai bao nhieu lan cung duoc
- Cuoi cung gop tat ca thanh 1 file TatCa_LoiNoi.txt de gui cho Claude doc

Cach dung:  python chep_loi.py "G:\\My Drive\\BRIAN SECOND 2\\cashflow" "C:\\Users\\...\\Desktop\\LoiNoi_KhoaHoc"
"""
import argparse
import os
import sys
import time
from pathlib import Path


def fmt(t):
    t = int(t)
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("nguon")
    ap.add_argument("dich")
    ap.add_argument("--model", default="small", help="tiny / base / small / medium / large-v3")
    args = ap.parse_args()

    nguon, dich = Path(args.nguon), Path(args.dich)
    thu_muc_txt = dich / "tung_video"
    thu_muc_txt.mkdir(parents=True, exist_ok=True)

    videos = sorted((p for p in nguon.rglob("*") if p.is_file()
                     and p.name.upper().startswith("DJI_") and p.suffix.upper() == ".MP4"),
                    key=lambda p: p.name)
    if not videos:
        sys.exit(f"Khong tim thay video DJI_*.MP4 nao trong {nguon}")
    print(f"Tim thay {len(videos)} video.")

    from faster_whisper import WhisperModel
    try:
        import ctranslate2
        co_gpu = ctranslate2.get_cuda_device_count() > 0
    except Exception:
        co_gpu = False
    print(f"Dang tai model '{args.model}' ({'GPU' if co_gpu else 'CPU'}) - lan dau se tai ve vai tram MB...")
    model = WhisperModel(args.model, device="cuda" if co_gpu else "cpu",
                         compute_type="float16" if co_gpu else "int8")

    for i, v in enumerate(videos, 1):
        out = thu_muc_txt / (v.stem + ".txt")
        if out.exists() and out.stat().st_size > 0:
            print(f"[{i}/{len(videos)}] {v.name}: da co, bo qua")
            continue
        print(f"[{i}/{len(videos)}] {v.name} ({v.stat().st_size / 2**30:.2f} GB) ...", flush=True)
        bat_dau = time.time()
        try:
            segs, info = model.transcribe(str(v), language="vi", vad_filter=True, beam_size=5)
            dong = [f"[{fmt(s.start)}] {s.text.strip()}" for s in segs]
        except Exception as e:  # file hong / chua tai xong
            print(f"   LOI: {e}")
            continue
        vi_tri = v.parent.relative_to(nguon).as_posix() if v.parent != nguon else "(goc)"
        noi_dung = [f"# {v.name}", f"# Thu muc: {vi_tri}",
                    f"# Thoi luong: {fmt(info.duration)}", ""] + (dong or ["(khong co tieng noi)"])
        tmp = out.with_suffix(".tmp")
        tmp.write_text("\n".join(noi_dung) + "\n", encoding="utf-8")
        os.replace(tmp, out)
        print(f"   xong sau {time.time() - bat_dau:.0f}s, {len(dong)} doan")

    tong = dich / "TatCa_LoiNoi.txt"
    with open(tong, "w", encoding="utf-8") as f:
        for v in videos:
            p = thu_muc_txt / (v.stem + ".txt")
            if p.exists():
                f.write(p.read_text(encoding="utf-8") + "\n" + "=" * 60 + "\n\n")
    print(f"\nHOAN TAT. Gui file nay cho Claude:\n  {tong}")


if __name__ == "__main__":
    main()
