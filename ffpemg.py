import subprocess;
def video_to_ts(video_path):
    ts_all = "~/PycharmProjects/test1/ts_single.ts"
    cmd_str = f'/Users/xyz/Downloads/ffmpeg -y -i {video_path} -vcodec copy -acodec copy -vbsf h264_mp4toannexb {ts_all}'
    subprocess.run(cmd_str, encoding="utf-8", shell=True)
    print(f'从 {video_path} 转换到 {cmd_str} 成功！')

def ts_to_m3u8(ts_single, singlg_time):
    cmd_str = f'/Users/xyz/Downloads/ffmpeg -i {ts_single} -c copy -map 0 -f segment -segment_list temp_playlist.m3u8 -segment_time {singlg_time} ~/PycharmProjects/test1/ts_all/%03d.ts'
    subprocess.run(cmd_str, encoding="utf-8", shell=True)
    print(f'从 {ts_single} 转换到 temp_playlist.m3u8 成功！')

if __name__ == '__main__':
    # video_to_ts('/Users/xyz/Downloads/1.mp4')
    ts_to_m3u8('~/PycharmProjects/test1/ts_single.ts', '5');
