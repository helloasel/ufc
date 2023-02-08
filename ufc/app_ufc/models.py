from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Весовая категория')
    info = models.TextField(verbose_name='')
    image = models.ImageField(verbose_name='', upload_to='photo_trainer/%Y/%m/%d')


    class Meta:
        verbose_name = ''
        verbose_name_plural = ''


    def __str__(self):
        return self.name


class Sportman(models.Model):
    CATEGORY = (
                ('w_1','Наилегчайший вес'),
                ('w_2','Легчайший вес'),
                ('w_3','Полулёгкий вес'),
                ('w_4','Легкий вес '),
                ('w_5','Полусредний вес'),
                ('w_6','Средний вес'),
                ('w_7','Полутяжёлый вес'),
                ('w_8','Тяжёлый вес'),
                )
    category = models.CharField(max_length=3,choices=CATEGORY)
    name = models.CharField(max_length=200, verbose_name='Ф.И.О спортсмена')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    reiting = models.IntegerField(verbose_name='Рейтинг')
    
    

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''


    def __str__(self):
        return self.name

class Treiner(models.Model):
    name = models.CharField(max_length=200,verbose_name='Ф.И.О тренера')
    image = models.ImageField(verbose_name='Фотка Информация о тренере ', upload_to='photoTrainer/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
    

class News(models.Model):
    news = models.TextField(verbose_name='Новости')
    data_publish = models.DateField(verbose_name='Дата публикации')


    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    instagram = models.CharField(max_length=500)
    youtube = models.CharField(max_length=500)
    name = models.CharField(max_length=20, verbose_name='')

    def __str__(self) -> str:
        return self.name



    
class Contact(models.Model):
    COOPERATION = (
        ('1','Журналисты'),
        ('2', 'Прямой эфир'),
        ('3','Бизнесмены'),
        ('4','Судьи'),
        
    )
    
    name = models.CharField(max_length=200, verbose_name='И.Ф.О для сотрудничества')
    number = models.IntegerField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Адрес электронной почты')
    massage = models.TextField(verbose_name='Сообщения о сотрудничестве')

    def __str__(self):
        return self.name
    
    
    

    





    

    

    
    

    
