mkdir -p data/raw data/interim data/external data/processed
touch data/external/.gitkeep data/raw/.gitkeep data/interim/.gitkeep data/processed/.gitkeep
git add -f data/external/.gitkeep data/processed/.gitkeep data/interim/.gitkeep data/raw/.gitkeep
git add .gitignore
git status

git commit -m "Empty data directories"