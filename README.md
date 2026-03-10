# Источники задач и контракты
## Лабораторная работа №1.
**Иванющенко Эрик Александрович. М8О-104БВ-25**

---
## Начало работы
```bash
uv vevn
uv sync
source .venv/bin/activate
# для Windows: .venv\Scripts\activate
```

## Запуск
```bash
python -m src.main
```

---
## Реализованные классы
### Task
Датакласс хранящий id и payload задачи. В данном случае это строки

### TaskSource
Протокол для других источников задач. ```@runtime_checkable``` позволяет проверять соответствие контракту в рантайме. Содержит метод ```get_tasks``` для получения задач

### TaskSourceJSON
Источник задач, который парсит из JSON файла

### TaskSourceGen
Источник задач, генерирующий задачи с помощью ```random```

### TaskSourceAPI
Источник задач, генерирующий задачи с задержкой по времени

## Покрытие
![](https://github.com/tau-lavender/laba_py_task/blob/main/img/cov.png)
