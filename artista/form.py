from django.forms import ModelForm
from.models import Musica

class MusicaForm(ModelForm):
    class Meta:
        model=Musica
        fields = [ 'nome', 'data_Post_Musc', 'duracao', 'youtube', 'spotify','artista','obesrvacoes']