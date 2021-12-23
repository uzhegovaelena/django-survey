from rest_framework import serializers
from .models import Survey, Question, Choice, Answer
from django.db.models import Q


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ('id', )


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Question.Type.choices, default=Question.Type.TEXT)
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'survey': {'write_only': True}
        }


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'
        read_only_fields = ('id', )


    # def create_choices(self, question, choices):
    #     Choice.objects.bulk_create([
    #         Choice(question=question, **d) for d in choices
    #     ])
    #
    # def create(self, validated_data):
    #     choices = validated_data.pop('choices', [])
    #     question = Question.objects.create(**validated_data)
    #     self.create_choices(question, choices)
    #     return question
    #
    # def update(self, instance, validated_data):
    #     choices = validated_data.pop('choices', [])
    #     instance.choices.all().delete()
    #     self.create_choices(instance, choices)
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #
    #     instance.save()
    #     return instance




    # def validate_start_date(self, value):
    #     """
    #     Raise error if try to change start_date after survey started.
    #     """
    #     if self.instance and self.instance.start_date < value:
    #         raise serializers.ValidationError(
    #             "Not allow change start_date survey is started"
    #         )
    #
    #     return value


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('id', )


# class VoteSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True)
#     survey = SurveySerializer(read_only=True)
    # survey_id = ObjectIDField(
    #     queryset=Survey.objects.filter(end_date__gte=datetime.date.today()),
    #     write_only=True
    # )

    # class Meta:
    #     model = Vote
    #     fields = ('id', 'survey_id', 'survey', 'user', 'date', 'answers')
    #     read_only_fields = ('id', 'user', 'date')

    # def create(self, validated_data):
    #     answers = validated_data.pop('answers', [])
    #     instance = Vote.objects.create(**validated_data)
    #     Answer.objects.bulk_create([
    #         Answer(vote=instance, **a) for a in answers
    #     ])
    #     return instance