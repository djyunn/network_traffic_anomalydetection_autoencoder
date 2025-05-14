# 네트워크 트래픽 기반 이상 탐지 시스템

## 프로젝트 개요
이 프로젝트는 네트워크 트래픽 데이터를 분석하여 이상 패턴을 탐지하고, 탐지된 이상에 대해 공격 유형을 분류하는 시스템입니다. Autoencoder를 사용하여 정상 데이터로부터 이상을 탐지하고, XGBoost를 활용하여 탐지된 이상의 공격 유형을 분류합니다. 이 시스템은 NSL-KDD 데이터셋을 사용하여 학습 및 평가되었습니다.

## 주요 기능
- **선형/비선형 체크** : 해당 데이터의 특징(선형/비선형)을 파악하고 이에 맞는 모델링 준비
- **데이터 전처리**: 범주형 변수의 원-핫 인코딩 및 수치형 변수의 표준화
- **Autoencoder 학습**: 정상 데이터를 학습하여 이상을 탐지하는 모델 구축
- **이상 탐지**: Autoencoder를 사용한 이상 탐지
- **XGBoost 학습**: 비정상 데이터로 XGBoost 모델을 학습해 공격 유형을 분류
- **공격 유형 분류**: 탐지된 이상에 대해 XGBoost로 공격 유형을 예측
- **성과 평가**: F1-Score를 사용해 이상 탐지와 공격 유형 분류 성능을 평가

## 설치 방법
1. **필요한 라이브러리 설치**:
   ```bash
   pip install pandas scikit-learn xgboost scipy keras
   ```
2. **데이터셋 준비**:
   - NSL-KDD 데이터셋의 `KDDTrain+.txt`와 `KDDTest+.txt` 파일을 다운로드하여 프로젝트 디렉토리에 저장합니다.

## 사용법
1. **데이터 전처리**:
   - `data_preprocessing.py`를 통해 데이터 로드 및 전처리 수행
2. **모델 학습 및 예측**:
   - `autoencoder.py`와 `xgboost_classifier.py`를 사용하여 모델 학습
   - `run.py`를 실행하여 전체 프로세스 수행
3. **성과 평가**:
   - `evaluation.py`를 통해 이상 탐지 및 공격 유형 분류 성능 평가

## 데이터셋
- **NSL-KDD**: 네트워크 침입 탐지 데이터셋으로, 정상 및 다양한 공격 유형의 트래픽 데이터를 포함합니다.
- **열 이름**: `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes`, `land`, `wrong_fragment`, `urgent`, `hot`, `num_failed_logins`, `logged_in`, `num_compromised`, `root_shell`, `su_attempted`, `num_root`, `num_file_creations`, `num_shells`, `num_access_files`, `num_outbound_cmds`, `is_host_login`, `is_guest_login`, `count`, `srv_count`, `serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`, `srv_diff_host_rate`, `dst_host_count`, `dst_host_srv_count`, `dst_host_same_srv_rate`, `dst_host_diff_srv_rate`, `dst_host_same_src_port_rate`, `dst_host_srv_diff_host_rate`, `dst_host_serror_rate`, `dst_host_srv_serror_rate`, `dst_host_rerror_rate`, `dst_host_srv_rerror_rate`, `label`

## 모델 설명
- **Autoencoder**: 정상 데이터를 학습하여 이상을 탐지하는 비지도 학습 모델입니다. 정상 데이터의 특성을 학습하고, 이에 벗어나는 데이터를 이상으로 간주합니다.
- **XGBoost**: 탐지된 이상 데이터에 대해 공격 유형을 분류하는 지도 학습 모델입니다. 다중 클래스 분류를 지원하며, 높은 성능을 제공합니다.

## 성능 평가
- **이상 탐지**: F1-Score를 사용하여 이상 탐지 성능을 평가합니다.
- **공격 유형 분류**: F1-Score를 사용하여 공격 유형 분류 성능을 평가합니다.

## 참고 사항
- **하이퍼파라미터**: Autoencoder의 `encoding_dim`과 XGBoost의 설정은 기본값을 사용했으나, 필요 시 튜닝이 가능합니다.
- **실행**: `run.py`를 실행하면 데이터 전처리, 모델 학습, 예측, 성능 평가가 자동으로 수행됩니다.
- **데이터셋 파일**: `KDDTrain+.txt`와 `KDDTest+.txt` 파일이 프로젝트 디렉토리에 있어야 합니다.