# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: [Родионов Михаил Юрьевич]

def get_system_info():
    system_info = {
        "student_name": "Родионов Михаил Юрьевич",
        "academic_group": "ИВТИИбд-11",
        "github_link": "https://github.com/Misha2110"
    }
    return system_info


if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
