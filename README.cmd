cd repo
python git_clone.py
cd ..
python generate_super_pom.py
cd repo
python mvn_validate.py
python find_result.py

