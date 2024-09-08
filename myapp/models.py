from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField
import uuid
from django.core.exceptions import ValidationError

class Alumni(models.Model):
    # String Fields
    first_name = models.CharField(max_length=100, null=False, blank=False)  # Required
    last_name = models.CharField(max_length=100, null=False, blank=False)  # Required
    bio = models.TextField(null=True, blank=True)  # Optional
    slug = models.SlugField(null=True, blank=True)  # Optional
    email = models.EmailField(null=False, blank=False, unique=True)  # Required and unique
    personal_website = models.URLField(null=True, blank=True)  # Optional
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto-generated unique identifier
    file_path = models.FilePathField(path="/your/file/path", null=True, blank=True)  # Optional

    # Numeric Fields
    graduation_year = models.PositiveIntegerField(null=False, blank=False)  # Required
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional
    integer_field = models.IntegerField(null=True, blank=True)  # Optional
    big_integer_field = models.BigIntegerField(null=True, blank=True)  # Optional
    positive_integer_field = models.PositiveIntegerField(null=True, blank=True)  # Optional
    small_integer_field = models.SmallIntegerField(null=True, blank=True)  # Optional
    positive_small_integer_field = models.PositiveSmallIntegerField(null=True, blank=True)  # Optional
    float_field = models.FloatField(null=True, blank=True)  # Optional
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional

    # Boolean Fields
    is_employed = models.BooleanField(default=True)  # Optional
    boolean_field = models.BooleanField(default=True)  # Optional

    # Date and Time Fields
    date_of_birth = models.DateField(null=False, blank=False)  # Required
    graduation_date = models.DateField(null=False, blank=False)  # Required
    time_field = models.TimeField(auto_now=True, null=True, blank=True)  # Optional
    datetime_field = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Optional
    duration_field = models.DurationField(null=True, blank=True)  # Optional

    # File and Image Fields
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Optional
    file_field = models.FileField(upload_to='uploads/', null=True, blank=True)  # Optional
    image_field = models.ImageField(upload_to='images/', null=True, blank=True)  # Optional

    # Relational Fields
    mentor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='mentees')  # Optional
    alumni_network = models.ManyToManyField('self', related_name='connected_alumni', blank=True)  # Optional
    one_to_one = models.OneToOneField('self', on_delete=models.CASCADE, related_name='one_to_one_related', null=True, blank=True)  # Optional

    # Miscellaneous Fields
    binary_field = models.BinaryField(null=True, blank=True)  # Optional
    ip_address_field = models.GenericIPAddressField(null=True, blank=True)  # Optional
    json_field = models.JSONField(null=True, blank=True)  # Optional

    # PostgreSQL Specific Fields
    array_field = ArrayField(models.IntegerField(), default=list, blank=True)  # Optional
    hstore_field = HStoreField(default=dict, blank=True)  # Optional

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Alumni"

    def clean(self):
        """
        Additional validation logic for the model, particularly the relationships.
        """
        super().clean()
        if self.mentor and self.mentor == self:
            raise ValidationError('An alumni cannot be their own mentor.')

        if self.alumni_network.filter(pk=self.pk).exists():
            raise ValidationError('An alumni cannot be in their own network.')

    def get_network_connections(self):
        """
        Retrieve all connected alumni in the network.
        """
        return self.connected_alumni.all()

    def get_mentor_details(self):
        """
        Fetch the mentor details.
        """
        return self.mentor if self.mentor else "No mentor assigned"



'''
{
  "first_name": "John",
  "last_name": "Doe",
  "bio": "An experienced software engineer with a passion for open-source projects.",
  "slug": "john-doe",
  "email": "john.doe@example.com",
  "personal_website": "https://johnsportfolio.com",
  "uuid": "a2b9c8d6-e99b-4a2b-b9c9-7e35e28d6c85",
  "file_path": "/path/to/file",
  "graduation_year": 2020,
  "current_salary": "75000.00",
  "integer_field": 123,
  "big_integer_field": 9876543210,
  "positive_integer_field": 100,
  "small_integer_field": 20,
  "positive_small_integer_field": 10,
  "float_field": 3.14,
  "decimal_field": "12345.67",
  "is_employed": true,
  "boolean_field": false,
  "date_of_birth": "1990-05-15",
  "graduation_date": "2020-06-15",
  "time_field": "14:30:00",
  "datetime_field": "2024-09-08T14:30:00Z",
  "duration_field": "1:30:00",
  "profile_picture": "profile_pics/john_doe.jpg",
  "file_field": "uploads/resume.pdf",
  "image_field": "images/john_doe_image.jpg",
  "mentor": null,
  "alumni_network": [2, 3, 4],  // Example IDs of connected alumni
  "one_to_one": null,
  "binary_field": "binarydata",
  "ip_address_field": "192.168.1.1",
  "json_field": {
    "interests": ["technology", "sports"],
    "languages": ["English", "Spanish"]
  },
  "array_field": [1, 2, 3, 4, 5],
  "hstore_field": {
    "key1": "value1",
    "key2": "value2"
  }
}

'''