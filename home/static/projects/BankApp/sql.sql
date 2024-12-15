create table transactions (
   t_id Char(64) PRIMARY KEY NOT NULL,
   rec_acc_no Char(64) NOT NULL,
   orig_acc_no Char(64) NOT NULL,
   _to Char(64) NOT NULL,
   amount Real NOT NULL,
   time_stamp DATETIME NOT NULL
);