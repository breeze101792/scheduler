#!/bin/bash
function generate_exc()
{
    local exc_file='xched'
    local cpath=`pwd`
    echo "#!/bin/bash" > $exc_file
    echo "pushd $cpath > /dev/null" >> $exc_file
    echo "source .venv/bin/activate" >> $exc_file
    echo "python3 $cpath/scheduler.py \$@" >> $exc_file
    echo "popd > /dev/null" >> $exc_file

    chmod u+x $exc_file

    echo "file has been sent to ${exc_file}"
}

function fHelp()
{
    echo "Setup Usage"
    printf "    %s%s%s\n" "-e|--exec" "->" "generate exec file"
    printf "    %s%s%s\n" "-h|--help" "->" "Help me"
    echo "Note."
    echo "      Step 1. Do submodule init/update"
    echo "      Step 2. Install p7zip-full, iconv, pyton3."
}

function setup()
{
    while [ "$#" != "0" ]
    do
        case $1 in
            -e|--exec)
                generate_exc
                ;;
            -h|--help)
                fHelp
                return 0
                ;;
            *)
                echo "Unknown Args"
                fHelp
                return 1
                ;;
        esac
        shift 1
    done
}
setup $@
