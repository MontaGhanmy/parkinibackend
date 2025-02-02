from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyUtilisateurManager(BaseUserManager):
    def create_user(self, email, username, password="changethis"):
        if not email:
            raise ValueError("User must have an email!")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    

class Utilisateur(AbstractUser):
    email = models.CharField(max_length=60, unique=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    num_tel = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_prop = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    objects = MyUtilisateurManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Parking(models.Model):
    UNITE_CHOICES = [
        ('H', '1 Hour'),
        ('30MINS', '30 Mins'),
        ('15MINS','15 Mins')
    ]
    owner = models.ForeignKey(Utilisateur,related_name="parkings" ,on_delete=models.CASCADE, null=True)
    name_parking = models.CharField(max_length=30, default="Parking")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    nb_places = models.IntegerField()
    nb_etages = models.IntegerField()
    heure_d_ouverture = models.TimeField()
    heure_d_fermeture = models.TimeField()
    jours_d_ouverture = ArrayField(models.BooleanField(default=False), size=8, default=list, null=True, blank=True)
    prix = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    unite_horaire = models.CharField(max_length=30, choices=UNITE_CHOICES)
    adresse = models.CharField(max_length=80)
    rating = models.DecimalField(max_digits=2,decimal_places=1, null=False, default=0)
    securise = models.BooleanField(default=False)
    barriere_auto = models.BooleanField(default=False)
    couvert = models.BooleanField(default=False)
    lavage = models.BooleanField(default=False)
    telepeage = models.BooleanField(default=False)
    WC = models.BooleanField(default=False)
    parking_image = models.ImageField(upload_to ='uploads/', blank=True, null=True)

class Place(models.Model):
    num_place = models.IntegerField()
    num_etage = models.IntegerField()
    zone = models.CharField(max_length=10)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)


class Voiture(models.Model):
    matricule = models.CharField(max_length=30)
    owner= models.ForeignKey(Utilisateur, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.pk)

class Occupation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class Notification(models.Model):
    t_user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE) # Target user
    t_car = models.ForeignKey(Voiture, on_delete=models.CASCADE) # Target voiture
    t_parking = models.ForeignKey(Parking, on_delete=models.CASCADE) # Target parking
    isConsulted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
    