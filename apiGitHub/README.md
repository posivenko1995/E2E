Задание GitHub API.
1.Добавить файлы "apiGitHub.py" и "Config.py" в pyCharm (или другую среду разработки).
2. Если не установлен модуль requests. В терминале pyCharm (или другой среды разработки) прописать команду "pip install requests".
3. В файле config.py изменить значение в переменных окружения:
        token = {''} - пример:token = {'Authorization': 'bearer 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'}
        usernameGitHub = "" - пример :usernameGitHub = "usernamegithub"
        namerepo = "" - пример:namerepo = "namerepositories"
4.Запустить код.
 Сценарий теста положительны. Oтвет на метод "post" и "get":сущности, ответ на метод "delete" "Response 204".
