from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self,email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un email')
        
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            # is_active = is_active,
            # is_staff = is_staff,
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, first_name, last_name,password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            # is_active=is_active,
            # is_staff=is_staff
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user 
    
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module_perms(self, app_label):
        return True 
    
    @property
    def is_staff(self):
        return self.is_admin     