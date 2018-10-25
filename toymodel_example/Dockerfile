#Dockerfile Toymodel with GRPC
FROM ubuntu:16.04
RUN apt-get update -y


#Install tools
RUN apt-get install -y git apt-utils software-properties-common build-essential python-numpy python-dev python-pip


#Install libraries
RUN pip install --upgrade pip
RUN pip install --upgrade numpy
RUN pip install pandas netcdf4 xarray datetime ConfigParser
#RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt-get update

#Configure and build
WORKDIR /opt
RUN pip install git+https://github.com/eWaterCycle/parametersetdb.git#egg=ewatercycle-parametersetdb
RUN pip install git+https://github.com/eWaterCycle/grpc4bmi.git#egg=grpc4bmi
RUN git clone https://github.com/eWaterCycle/ewatercycle-toymodels.git


#Install toymodel and bmi
ENV PYTHONPATH /usr/local/python/
WORKDIR /opt/ewatercycle-toymodels/
RUN python setup.py install
WORKDIR /opt/ewatercycle-toymodels/bmi/
RUN python setup.py install

VOLUME /data



#Set grpc4bmi
ENV BMI_MODULE = toymodel_lumped
ENV BMI_CLASS = toy_bmi

ENTRYPOINT ["run-bmi-server","--name","toymodel_lumped_bmi.toy_bmi","--port","55555","--path","/opt/ewatercycle-toymodels/"]
EXPOSE 55555


