import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# NSL-KDD 데이터 로드 (예: KDDTrain+.txt)
data = pd.read_csv('KDDTrain+.txt', header=None)
# 연속형 특성 선택 (예: 0번(duration), 5번(src_bytes), 6번(dst_bytes))
X = data[[0, 5, 6]]
X.columns = ['duration', 'src_bytes', 'dst_bytes']

# 데이터 정규화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 산점도 플롯
sns.pairplot(pd.DataFrame(X_scaled, columns=['duration', 'src_bytes', 'dst_bytes']))
plt.show()
