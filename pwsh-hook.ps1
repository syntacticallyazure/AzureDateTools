# ensure that the uv venv exists and dot source this file.

function today { 
    uv run python "$PSScriptRoot\src\today.py" @Args
}

function tomorrow { 
    uv run python "$PSScriptRoot\src\tomorrow.py" @Args
}

function yesterday { 
    uv run python "$PSScriptRoot\src\yesterday.py" @Args
}
