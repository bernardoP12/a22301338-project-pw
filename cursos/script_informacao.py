from django.db import transaction
from cursos.models import Curso, Disciplina, Docente, AreaCientifica, LinguagemProgramacao, Projeto
import json

def importar_curso(ficheiro_json):
    with open(ficheiro_json, 'r') as file:
        data = json.load(file)

        try:
            with transaction.atomic():
                # Create a new Curso instance
                curso = Curso.objects.create(
                    apresentacao=data['courseDetail']['presentation'],
                    objetivos=data['courseDetail']['objectives'],
                    competencias=data['courseDetail']['competences']
                )

                # Importação de Áreas Científicas e Disciplinas
                for area in data['courseFlatPlan']:
                    area_cientifica = AreaCientifica.objects.create(
                        nome=area['curricularUnitName'],
                        descricao=f"Descrição para {area['curricularUnitName']}"
                    )

                    # Create new Disciplina instances
                    disciplina = Disciplina.objects.create(
                        nome=area['curricularUnitName'],
                        ano=area['curricularYear'],
                        semestre=area['semester'],
                        ects=area['ects'],
                        curricularUnitReadableCode=area['curricularIUnitReadableCode'],
                        area_cientifica=area_cientifica
                    )

                print("Dados importados com sucesso!")
        except Exception as e:
            print(f"Erro ao importar dados: {e}")