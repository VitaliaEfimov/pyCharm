import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

# ---------- Группировка ответов ----------
# 1. Положительные
POSITIVE = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом"
]

# 2. Нерешительно положительные
CAUTIOUS_POSITIVE = [
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да"
]

# 3. Нейтральные / требующие уточнения
NEUTRAL = [
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять"
]

# 4. Отрицательные
NEGATIVE = [
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно"
]

# Общий массив (для обратной совместимости, если понадобится)
ALL_ANSWERS = POSITIVE + CAUTIOUS_POSITIVE + NEUTRAL + NEGATIVE

# Соответствие группы и цвета для отображения
GROUP_COLORS = {
    "POSITIVE": "#2ecc71",          # зелёный
    "CAUTIOUS_POSITIVE": "#f1c40f", # жёлто-золотой
    "NEUTRAL": "#3498db",           # синий
    "NEGATIVE": "#e74c3c"           # красный
}

class Magic8BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 Шар судьбы — Magic 8-Ball")
        self.root.geometry("650x550")
        self.root.resizable(True, True)
        self.root.configure(bg="#2c3e50")

        # История вопросов и ответов
        self.history = []

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Верхний заголовок
        title_label = tk.Label(
            self.root,
            text="🔮 Шар судьбы 🔮",
            font=("Arial", 24, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50",
            pady=10
        )
        title_label.pack()

        # Рамка для шара (имитация)
        self.ball_frame = tk.Frame(
            self.root,
            bg="#34495e",
            bd=5,
            relief=tk.RAISED,
            height=150
        )
        self.ball_frame.pack(pady=15, padx=20, fill=tk.X)

        self.answer_label = tk.Label(
            self.ball_frame,
            text="✨ Задай вопрос ✨",
            font=("Arial", 16, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            wraplength=500,
            justify="center"
        )
        self.answer_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)

        # Поле ввода вопроса
        question_frame = tk.Frame(self.root, bg="#2c3e50")
        question_frame.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(
            question_frame,
            text="Ваш вопрос:",
            font=("Arial", 12),
            fg="#ecf0f1",
            bg="#2c3e50"
        ).pack(anchor=tk.W)

        self.question_entry = tk.Entry(
            question_frame,
            font=("Arial", 12),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief=tk.SUNKEN,
            bd=2
        )
        self.question_entry.pack(fill=tk.X, pady=5)
        self.question_entry.bind("<Return>", lambda event: self.ask_question())

        # Кнопка получения ответа
        self.ask_button = tk.Button(
            self.root,
            text="🎱 Тряхнуть шар 🎱",
            font=("Arial", 14, "bold"),
            bg="#e67e22",
            fg="white",
            activebackground="#d35400",
            cursor="hand2",
            command=self.ask_question
        )
        self.ask_button.pack(pady=10)

        # История (прокручиваемое поле)
        history_frame = tk.Frame(self.root, bg="#2c3e50")
        history_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        tk.Label(
            history_frame,
            text="📜 История вопросов и ответов:",
            font=("Arial", 10, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        ).pack(anchor=tk.W)

        self.history_text = scrolledtext.ScrolledText(
            history_frame,
            font=("Courier New", 10),
            bg="#ecf0f1",
            fg="#2c3e50",
            wrap=tk.WORD,
            height=12,
            state=tk.DISABLED
        )
        self.history_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Кнопка очистки истории
        clear_button = tk.Button(
            self.root,
            text="🗑 Очистить историю",
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            cursor="hand2",
            command=self.clear_history
        )
        clear_button.pack(pady=5)

        # Статусная строка (группа последнего ответа)
        self.status_label = tk.Label(
            self.root,
            text="Готов к вопросам",
            font=("Arial", 9, "italic"),
            fg="#bdc3c7",
            bg="#2c3e50",
            pady=5
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def get_answer_group(self, answer):
        """Определяет группу ответа и возвращает (группа, цвет)"""
        if answer in POSITIVE:
            return "POSITIVE", GROUP_COLORS["POSITIVE"]
        elif answer in CAUTIOUS_POSITIVE:
            return "CAUTIOUS_POSITIVE", GROUP_COLORS["CAUTIOUS_POSITIVE"]
        elif answer in NEUTRAL:
            return "NEUTRAL", GROUP_COLORS["NEUTRAL"]
        else:
            return "NEGATIVE", GROUP_COLORS["NEGATIVE"]

    def get_random_answer(self):
        """Выбирает случайный ответ из общего массива (с учётом всех групп)"""
        return random.choice(ALL_ANSWERS)

    def ask_question(self):
        """Основной метод: получить вопрос, сгенерировать ответ, добавить в историю"""
        question = self.question_entry.get().strip()

        if not question:
            messagebox.showwarning("Пустой вопрос", "Пожалуйста, введите ваш вопрос.")
            return

        # Получаем случайный ответ
        answer = self.get_random_answer()
        group, color = self.get_answer_group(answer)

        # Обновляем "шар" (метку с ответом)
        self.answer_label.config(text=f"🎱 {answer} 🎱", fg=color)

        # Добавляем в историю
        history_entry = f"❓ {question}\n🔮 {answer} ( {group.replace('_', ' ')} )\n{'-'*50}\n"
        self.history.append(history_entry)

        # Обновляем виджет истории
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, history_entry)
        self.history_text.see(tk.END)  # автоскролл вниз
        self.history_text.config(state=tk.DISABLED)

        # Обновляем статус
        group_ru = {
            "POSITIVE": "положительный",
            "CAUTIOUS_POSITIVE": "нерешительно положительный",
            "NEUTRAL": "нейтральный",
            "NEGATIVE": "отрицательный"
        }.get(group, "неизвестный")

        self.status_label.config(text=f"Последний ответ: {group_ru} | Всего вопросов: {len(self.history)}")

        # Очищаем поле ввода для следующего вопроса
        self.question_entry.delete(0, tk.END)

        # Небольшая анимация (мигание шара)
        self.animate_ball()

    def animate_ball(self):
        """Простая анимация: меняем цвет рамки на пару секунд"""
        original_bg = self.ball_frame.cget("bg")
        self.ball_frame.config(bg="#f39c12")
        self.root.after(200, lambda: self.ball_frame.config(bg=original_bg))

    def clear_history(self):
        """Очищает историю"""
        if messagebox.askyesno("Очистка истории", "Вы уверены, что хотите очистить всю историю?"):
            self.history.clear()
            self.history_text.config(state=tk.NORMAL)
            self.history_text.delete(1.0, tk.END)
            self.history_text.config(state=tk.DISABLED)
            self.status_label.config(text="История очищена")
            self.root.after(1500, lambda: self.status_label.config(text=f"Готов к вопросам"))

if __name__ == "__main__":
    root = tk.Tk()
    app = Magic8BallApp(root)
    root.mainloop()