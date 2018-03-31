from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    pass_word = models.CharField(max_length=60)
    father_name = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    year = models.IntegerField()
    sem = models.IntegerField()
    branch = models.CharField(max_length=60)
    admission_number = models.CharField(max_length=20)
    ten_res = models.FloatField()
    puc_res = models.FloatField()
    reg_no = models.CharField(max_length=25, primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=120)
    fee = models.IntegerField()
    rank = models.IntegerField()
    Temp_address = models.CharField(max_length=800)
    per_address = models.CharField(max_length=800)
    studying_year = models.CharField(max_length=9)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.reg_no


class Fee_pay(models.Model):
    paid_date = models.DateTimeField()
    fee_paid = models.IntegerField()
    card_no = models.CharField(max_length=25)
    trans_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.trans_id)


class Compliant(models.Model):
    add_date = models.DateField()
    status = models.CharField(max_length=120)
    explain = models.CharField(max_length=800)
    about = models.CharField(max_length=60)
    sub = models.CharField(max_length=200)
    comp_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.comp_id)


class Comp_match(models.Model):
    match_id = models.ForeignKey(Compliant, on_delete=models.CASCADE)
    regno = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_id) + " " + str(self.regno)


class Paying(models.Model):
    pay_id = models.ForeignKey(Fee_pay, on_delete=models.CASCADE)
    std_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pay_id) + " " + str(self.std_id)


class Defuser(models.Model):
    user_name = models.CharField(max_length=60)
    pass_word = models.CharField(max_length=60)
    user_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.user_id)

    def ret(self):
        return self.user_id

class Notif(models.Model):
    added_date = models.DateField()
    expiry_date = models.DateField()
    posted_by_id = models.ForeignKey(Defuser, on_delete=models.CASCADE)
    data = models.CharField(max_length=1500)
    head = models.CharField(max_length=500)

    def __str__(self):
        return str(self.added_date) + " " + str(self.posted_by_id) + " " + str(self.head) + " " + str(self.data)

