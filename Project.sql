/* TABLE CREATION  */

create table passenger(
PassengerID int(8) primary key,
PassengerName char(25) not null,
Age int(3),
Gender char(1),
FlightNo varchar(6) not  null);

create table flight(
FlightNo varchar(6) references passenger(FlightNo),
Airlines char(10) not null,
Destination char(10) not null);


/* INSERTION INTO FLIGHT */

insert into flight values('AI5674','Air India','New Delhi');
insert into flight values('IG6678','IndiGo','New Delhi');
insert into flight values('AI9975','Air India','New Delhi');
insert into flight values('AI3625','Air India','New Delhi');
insert into flight values('AI8281','Air India','Chennai');
insert into flight values('IG8179','IndiGo','Chennai');
insert into flight values('VS1910','Vistara','Chennai');
insert into flight values('VS8271','Vistara','Chennai');
insert into flight values('VS7718','Vistara','New Delhi');




/* INSERTION INTO PASSENGER */

insert into passenger values('0001','Rishabh',16,'M','AI5674');
insert into passenger values('0002','Abhishek',24,'M','IG8179');
insert into passenger values('0003','Aayush',18,'M','VS8271');
insert into passenger values('0004','Seher',21,'F','VS7718');
insert into passenger values('0005','Vishakha',30,'F','IG8179');
insert into passenger values('0006','Saksham',30,'M','AI5674');
insert into passenger values('0007','Sambhav',56,'M','AI9975');
insert into passenger values('0008','Shagun',37,'F','IG6678');
insert into passenger values('0009','Shobha',65,'F','VS1910');
insert into passenger values('0010','Sanjay',46,'M','AI8281');
insert into passenger values('0011','Pradeep',78,'M','AI3625');
insert into passenger values('0012','Unnati',12,'F','AI3625');
insert into passenger values('0013','Khushi',26,'F','AI8281');
insert into passenger values('0014','Garima',44,'F','AI5674');
insert into passenger values('0015','Himanshu',33,'M','VS7718');
insert into passenger values('0016','Nilansha',16,'F','VS8271');
insert into passenger values('0017','Shaurya',17,'M','AI9975');
insert into passenger values('0018','Abreesh',19,'M','VS7718');
insert into passenger values('0019','Pranav',78,'M','AI9975');
insert into passenger values('0020','Anuvrinda',23,'F','IG6678');
insert into passenger values('0021','Manasvi',55,'F','VS1910');
insert into passenger values('0022','Aryama',16,'F','AI5674');
insert into passenger values('0023','Ajay',51,'M','AI8281');
insert into passenger values('0024','Shobit',36,'M','AI9975');
insert into passenger values('0025','Yagya',14,'M','IG6678');
insert into passenger values('0026','Soumil',15,'M','IG6678');
insert into passenger values('0027','Suhana',34,'F','VS8271');
insert into passenger values('0028','Akansha',23,'F','VS8271');
insert into passenger values('0029','Megha',29,'F','AI8281');
insert into passenger values('0041','Suhana',34,'F','VS8271');
insert into passenger values('0042','Akansha',23,'F','VS8271');
insert into passenger values('0043','Megha',29,'F','AI8281');
insert into passenger values('0030','Sarthak',05,'M','AI5674');
insert into passenger values('0031','Bina',98,'F','AI9975');
insert into passenger values('0032','Chauhan',29,'M','IG6678');
insert into passenger values('0033','Dharmendra',29,'M','IG6678');
insert into passenger values('0034','Vijay',89,'M','VS8271');
insert into passenger values('0035','Komal',49,'F','AI5674');
insert into passenger values('0036','Arushi',49,'F','AI5674');
insert into passenger values('0037','Devika',28,'F','AI3625');
insert into passenger values('0038','Harsimran',28,'M','IG8179');
insert into passenger values('0039','Parth',15,'M','AI8281');
insert into passenger values('0040','Nilesh',33,'M','AI5674');
