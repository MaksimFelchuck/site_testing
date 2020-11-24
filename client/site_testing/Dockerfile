FROM python:3.8
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

ADD . / . /site_testing /client/
WORKDIR /client/site_testing/

RUN pip install -r requirements.txt



ENTRYPOINT "python3.8" "site_testing.py" "sql_injection_scanner" "http://localhost:5000/users?rank=user" && "python3.8" "site_testing.py" "xss_vulnerability_scanner" "http://localhost:5000/xss" && "python3.8" "site_testing.py" "check_link" "http://localhost:5000/" "Help" && "python3.8" "site_testing.py" "doctype_check" "http://localhost:5000/" && "python3.8" "site_testing.py" "find_link" "http://localhost:5000/" "/help" && "python3.8" "site_testing.py" "js_errors_check" "http://localhost:5000/"







