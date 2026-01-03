import numpy as np
import pandas as pd

def make_burger_potato_dataset(
    n_days=30,
    seed=42,
    burger_min=80,
    burger_max=220,
    slope=0.55,          # バーガーが1増えるとポテトが平均何増えるか
    intercept=5,         # 基本の上乗せ
    noise_sd=12,         # ばらつき（大きいほど散布図が散る）
    add_outliers=False,
):
    rng = np.random.default_rng(seed)

    # 日付（任意）：連番でも良いが、曜日があると「現場っぽい」
    dates = pd.date_range("2026-01-01", periods=n_days, freq="D")
    dow_map = ["月", "火", "水", "木", "金", "土", "日"]
    dows = [dow_map[d.weekday()] for d in dates]

    # x: ハンバーガー注文数（整数）
    burgers = rng.integers(burger_min, burger_max + 1, size=n_days)

    # y: ポテト注文数（線形 + ノイズ）
    noise = rng.normal(0, noise_sd, size=n_days)
    potatoes = slope * burgers + intercept + noise

    # 端数処理・負値対策（注文数なので0未満はあり得ない）
    potatoes = np.clip(np.round(potatoes), 0, None).astype(int)

    memo = [""] * n_days

    if add_outliers:
        # 外れ値：品切れでポテトが少ない日
        i1 = rng.integers(0, n_days)
        memo[i1] = "品切れ（ポテトが売り切れ）"
        potatoes[i1] = max(0, int(potatoes[i1] * 0.2))

        # 外れ値：イベントでポテトが妙に売れる日（セットキャンペーンなど）
        i2 = (i1 + rng.integers(5, 12)) % n_days
        memo[i2] = "セット割キャンペーン（ポテトが伸びた）"
        potatoes[i2] = int(potatoes[i2] * 1.5)

    df = pd.DataFrame({
        "日付": dates.strftime("%Y-%m-%d"),
        "曜日": dows,
        "ハンバーガー注文数": burgers,
        "ポテト注文数": potatoes,
        "メモ": memo
    })
    return df

# 生成
dataset_clean = make_burger_potato_dataset(add_outliers=False, seed=1)
dataset_outlier = make_burger_potato_dataset(add_outliers=True, seed=2)

# 保存（CSV）
dataset_clean.to_csv("burger_potato_clean.csv", index=False, encoding="utf-8-sig")
dataset_outlier.to_csv("burger_potato_outlier.csv", index=False, encoding="utf-8-sig")

# 保存（Excel：2シート）
with pd.ExcelWriter("burger_potato_datasets.xlsx", engine="openpyxl") as writer:
    dataset_clean.to_excel(writer, sheet_name="clean", index=False)
    dataset_outlier.to_excel(writer, sheet_name="outlier", index=False)

print("出力完了: burger_potato_clean.csv, burger_potato_outlier.csv, burger_potato_datasets.xlsx")
