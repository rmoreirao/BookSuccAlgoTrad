- Status: "Retrieving Data from the Securities Master"

- Other Requirements:
MySQL Community Server 8.0.13: admin
Microsoft Visual C++ 14.0 (https://www.scivision.co/python-windows-visual-c++-14-required/)

- To install new environment:
1) From C:\LocalDev\GitHub, run: git clone URL
2) From C:\LocalDev\GitHub, run: python -m venv BookSuccAlgoTrad\venv\
3) From C:\LocalDev\GitHub\BookSuccAlgoTrad, run: venv\Scripts\activate
4) From C:\LocalDev\GitHub\BookSuccAlgoTrad, run: pip install --requirement requirements.txt

5) For mysql: pip install --only-binary :all: mysqlclient

6) Run the SQL scripts and PY scripts under "init_scripts" folder.
   Can search "Configuring MySQL" in the Book.

- IB TWS:
User Name: edemo
Password: demouser

- Helpers:
pip freeze > requirements.txt

