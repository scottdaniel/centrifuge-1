BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
    PATH=/app/centrifuge:/app/stampede-centrifuge/scripts:$PATH
    LD_LIBRARY_PATH=/app
    export LD_LIBRARY_PATH

%runscript
    exec /app/centrifuge/centrifuge "$@"

%post
    apt-get update
    apt-get install -y locales git build-essential wget curl zip libcurl4-openssl-dev libssl-dev python3 python3-pip
    locale-gen en_US.UTF-8

    #
    # Put everything into $APP_DIR
    #
    export APP_DIR=/app
    mkdir -p $APP_DIR
    cd $APP_DIR

    wget -O centrifuge.zip ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/downloads/centrifuge-1.0.3-beta-Linux_x86_64.zip
    unzip centrifuge.zip
    mv centrifuge-1.0.3-beta centrifuge

    git clone https://github.com/hurwitzlab/stampede-centrifuge.git
    python3 -m pip install biopython

    #
    # Add CRAN to sources to get latest R
    #
    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
    gpg -a --export E084DAB9 | apt-key add -
    echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | \
        tee -a /etc/apt/sources.list
    apt-get install -y r-base r-base-dev

    cat << EOF > .Rprofile
local({
  r = getOption("repos")
  r["CRAN"] = "http://mirrors.nics.utk.edu/cran/"
  options(repos = r)
})
EOF
    /usr/bin/Rscript /app/stampede-centrifuge/scripts/install.r

    #
    # Mount points for TACC directories
    #
    mkdir /home1
    mkdir /scratch
    mkdir /work