from diaries.AbstractDiary import AbstractDiary

class MasashiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "今日は友達と遊んだ"
    def get_author(self):
        return "Masashi"