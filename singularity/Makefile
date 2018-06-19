<<<<<<< HEAD
SING242 = /usr/local/bin/singularity #2.4.2-dist
SING231 = /home/vagrant/bin/singularity #2.3.1-dist

SINGULARITY = $(SING231)
IMG_NAME = centrifuge-patric.img
||||||| merged common ancestors
SINGULARITY = /usr/local/bin/singularity
IMG_NAME = centrifuge-1.0.3-beta.img
=======
SINGULARITY = /usr/local/bin/singularity
IMG_NAME = centrifuge-1.0.4.img
>>>>>>> 6cdbc66c6abced72fd41ebe182361bf4dd23acc7
DEF_NAME = image.def
SIZE = 3036

run:
	sudo $(SINGULARITY) run $(IMG_NAME)

clean:
	rm -f $(IMG_NAME)

<<<<<<< HEAD
img: clean 
	#sudo $(SINGULARITY) build $(IMG_NAME) $(DEF_NAME) #actually the 2.4.2 way
||||||| merged common ancestors
img: clean
	#sudo $(SINGULARITY) build $(IMG_NAME) $(DEF_NAME)
=======
img: clean
>>>>>>> 6cdbc66c6abced72fd41ebe182361bf4dd23acc7
	sudo $(SINGULARITY) create --size $(SIZE) $(IMG_NAME)
	sudo $(SINGULARITY) bootstrap $(IMG_NAME) $(DEF_NAME)

shell:
<<<<<<< HEAD
	sudo $(SINGULARITY) shell --writable -B /vagrant:/work $(IMG_NAME)

scp:
	scp $(IMG_NAME) stampede2:/work/03859/sdaniel/stampede2/centrifuge-patric-0.0.5/stampede/
||||||| merged common ancestors
	sudo $(SINGULARITY) shell --writable -B $(shell pwd):/tmp $(IMG_NAME)

scp:
	scp $(IMG_NAME) stampede:/work/03137/kyclark/centrifuge-0.0.2/stampede
=======
	sudo $(SINGULARITY) shell --writable -B $(shell pwd):/tmp $(IMG_NAME)
>>>>>>> 6cdbc66c6abced72fd41ebe182361bf4dd23acc7
