import pytest
from main import *
@pytest.mark.parametrize(
'mentors1, expected', [
[mentors, 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена,'
            ' Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена,'
            ' Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат,'
            ' Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий']
]
    )
def test1(mentors1, expected):
    res = find_uniq_names(mentors1)
    assert res == expected
@pytest.mark.parametrize(
    'mentors1, expected', [
        [mentors, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']
    ]
)
def test2(mentors1, expected):
    res = top_3_names(mentors1)
    assert res == expected
@pytest.mark.parametrize(
    'mentors1, expected', [
        [mentors, "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим\n"
                  "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман\n"
                  "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений\n"
                  "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим\n"
                  "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений\n"
                  "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар\n"]
         ]
)
def test3(mentors1, expected):
    res = supername(mentors1)
    assert res == expected
