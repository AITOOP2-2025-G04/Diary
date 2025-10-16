from diaries.DiarySample import DiarySample
from diaries.MasashiDiary import MasashiDiary
from diaries.kounosukeDiary import kounosukeDiary
from diaries.IshimaruDiary import IshimaruDiary
from diaries.sankenDiary import sankenDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), MasashiDiary(), kounosukeDiary(), IshimaruDiary(), sankenDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()