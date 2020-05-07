from django.db import models
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
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    nb_places = models.IntegerField()
    nb_etages = models.IntegerField()
    heure_d_ouverture = models.TimeField()
    heure_d_fermeture = models.TimeField()
    prix = models.IntegerField()
    unite_horaire = models.CharField(max_length=30, choices=UNITE_CHOICES)
    adresse = models.CharField(max_length=30)
    securise = models.BooleanField(default=False)
    barriere_auto = models.BooleanField(default=False)
    couvert = models.BooleanField(default=False)

class Place(models.Model):
    num_etage = models.IntegerField()
    num_zone = models.CharField(max_length=10)
    parking = models.OneToOneField(Parking, on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)


class Voiture(models.Model):
    matricule = models.CharField(max_length=30)
    owner= models.OneToOneField(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

class Reservation(models.Model):
    voiture = models.OneToOneField(Voiture, on_delete=models.CASCADE)
    place = models.OneToOneField(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

class Occupation(Reservation):

    isCompleted = models.BooleanField(default=False)
    date_debut = models.DateTimeField(auto_now=True)
    date_fin = models.DateTimeField()

    def __str__(self):
        return self.pk