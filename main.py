import time
import wave
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()


# Читаем wav-файл, считываем его фреймы и преобразуем их в одномерный массив
wav = wave.open('4.wav', 'rb')
frames = wav.readframes(wav.getnframes())
framerate = wav.getframerate()
signal = np.frombuffer(frames, dtype=np.int16)


# Отображаем график первых 100 фреймов в зависимости от их амплитуды
plt.figure(figsize=(10, 4))
plt.bar(range(100), signal[:100])
plt.title('Звуковые сигналы')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

# Отображаем график времени от амплитуды звукового сигнала
times = np.arange(len(signal)) / wav.getframerate()
plt.figure(figsize=(10, 4))
plt.plot(times, signal, label='Осциллограмма')
plt.title('Осциллограмма сигнала')
plt.xlabel("Время, c")
plt.ylabel("Амплитуда")
plt.legend()
plt.grid(True)
plt.show()


# Спектральный анализ
n = len(signal)
spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(n, d=1/framerate)
phase = np.arctan2(np.imag(spectrum), np.real(spectrum))
plt.plot(np.abs(frequencies[:n//2]), phase[:n//2])
plt.title("Фаза ДПФ звукового сигнала")
plt.xlabel("Частота (Герц)")
plt.ylabel("Фаза ДПФ")
plt.grid(True)
plt.show()

print(time.time() - start_time, "seconds")

