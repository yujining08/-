import numpy as np
import matplotlib.pyplot as plt

# 총 시간(분)
total_time = 6 * 60  # 6시간
time = np.linspace(0, total_time, total_time)

# 수면 주기 설정 (90분 주기)
cycle_duration = 90
num_cycles = total_time // cycle_duration

# 수면 단계 계산 (사인 함수 기반)
# 비렘수면(NREM)은 음수, 렘수면(REM)은 양수로 나타냄
sleep_stage = np.sin(2 * np.pi * time / cycle_duration)

# 렘수면 구간 강조
rem_stage = np.where(sleep_stage > 0.8, sleep_stage, np.nan)  # y 값이 0.8 이상인 구간을 렘수면으로 표시

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(time, sleep_stage, label='Sleep Stage (NREM & REM)', color='b')
plt.plot(time, rem_stage, label='REM Sleep', color='r', linewidth=2)

# 그래프 꾸미기
plt.axhline(0, color='gray', linestyle='--')  # 기준선
plt.xlabel('Time (minutes)')
plt.ylabel('Sleep Stage Depth')
plt.title('Sleep Cycle Visualization (REM and NREM)')
plt.legend()
plt.grid(True)
plt.show()