import numpy as np
import librosa
import pyaudio
import wave
import os
import matplotlib.pyplot as plt
from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.audio import Pipeline
import speech_recognition as sr

# 환경 설정
os.environ["SB_LOCAL_STRATEGY"] = "true"

# 1. 오디오 녹음
def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    print("Recording...")

    frames = []
    for _ in range(0, int(16000 / 1024 * 5)):  # 5초 녹음
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return frames

# 2. 오디오 파일 저장
def save_audio_file(audio_data, filename="two_people.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(b''.join(audio_data))

# 3. Speaker Diarization 수행
def diarize_audio(filename):
    pipeline = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization")
    print(f"Running diarization on {filename}...")
    diarization = pipeline(filename)
    
    diarization_results = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        diarization_results.append((turn.start, turn.end, speaker))
        print(f"Speaker {speaker}: {turn.start:.1f}s to {turn.end:.1f}s")
    
    return diarization_results

# 4. Speaker Diarization 시각화

def plot_diarization(diarization_results):
    # 튜플의 첫 번째 요소는 시작 시간, 세 번째 요소는 speaker 이름
    times = [segment[0] for segment in diarization_results]
    speakers = [segment[2] for segment in diarization_results]

    plt.figure(figsize=(10, 5))
    plt.scatter(times, speakers, c='blue', marker='o')
    plt.xlabel("Time (s)")
    plt.ylabel("Speaker")
    plt.title("Speaker Diarization Result")
    plt.show()

# 전체 오디오 처리 실행
def process_audio():
    audio_data = record_audio()
    save_audio_file(audio_data, "two_people.wav")
    diarization_result = diarize_audio("two_people.wav")
    
    if diarization_result:
        plot_diarization(diarization_result)
    
    return diarization_result  # 다이어리제이션 결과를 반환하도록 추가

diarization_results = process_audio()
print(type(diarization_results))  # 타입 확인
print(diarization_results)  # 값 확인


