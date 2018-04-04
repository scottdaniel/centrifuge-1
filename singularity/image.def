BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
    PATH=/app/miniconda:/app/centrifuge:/app/stampede-centrifuge/scripts:$PATH
    LD_LIBRARY_PATH=/app
    export LD_LIBRARY_PATH

%runscript
    exec /app/stampede-centrifuge/scripts/launch_centrifuge.py "$@"

%post
	echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get upgrade

	#essential stuff
    apt -y --allow-downgrades install git sudo man vim build-essential wget unzip perl curl gdebi-core zip locales libcurl4-openssl-dev libssl-dev cpanminus
    locale-gen en_US.UTF-8

    #
    # Put everything into $APP_DIR
    #
    export APP_DIR=/app
    mkdir -p $APP_DIR
    cd $APP_DIR

    wget https://github.com/PATRIC3/PATRIC-distribution/releases/download/1.018/patric-cli-1.018.deb
    sudo gdebi -n patric-cli-1.018.deb
    cpanm install Class::Accessor
    git clone https://github.com/SEEDtk/RASTtk.git
    cp -r -n RASTtk/lib/* /usr/share/patric-cli/deployment/lib/

    wget -O centrifuge.zip ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/downloads/centrifuge-1.0.3-beta-Linux_x86_64.zip
    unzip centrifuge.zip
    mv centrifuge-1.0.3-beta centrifuge

    git clone https://github.com/scottdaniel/centrifuge-1.git --branch RADCOT \
        --single-branch stampede-centrifuge
    
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /app/miniconda
	rm Miniconda3-latest-Linux-x86_64.sh 
    sudo ln -s /app/miniconda/bin/python /usr/bin/python
    PATH="/app/miniconda/bin:$PATH"
	conda install -y -c conda-forge plumbum
	conda install -y -c bioconda biopython

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

    # 
    # Mount points for Ocelote if needed
    # 
    #mkdir /extra 
    #mkdir /xdisk 
    #mkdir /rsgrps
