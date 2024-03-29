$CurrentFolder = Get-Location | Split-Path -Leaf
$EnvFolder = "$CurrentFolder-venv"

if (Test-Path $EnvFolder) {
    Invoke-Expression "./$EnvFolder/Scripts/Activate.ps1"
} else {
    python -m venv $EnvFolder `
        && Invoke-Expression "./$EnvFolder/Scripts/Activate.ps1" `
        && pip install -r requirements.txt `

    cd ./py-build-utils && python setup.py install && cd ..

    python setup.py install
}