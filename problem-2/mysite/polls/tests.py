import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice
# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days=0):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_question(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

    # def test_no_choice_question(self):
    #     question = create_question(question_text="No Choice Question.")
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(
    #     response.context['latest_question_list'],
    #     []
    #     )
    #
    # def test_with_choices_question(self):
    #     question = create_question(question_text="With Choice Question.")
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         [question]
    #     )
    #
    # def test_no_choice_and_with_choices_question(self):
    #     question= create_question(question_text="With Choices Question.")
    #     create_question(question_text="No Choices Question.")
    #     response = self.client.get(reverse('polls:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         [question],
    #     )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultsViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future Question.', days=30)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    def test_no_choice_question(self):
        no_choice_question = create_question(question_text='No Choice Question.')
        url = reverse('polls:results', args=(no_choice_question.id,))
        response = self.client.get(url)
        self.assertContains(response, no_choice_question.question_text)

# class AdminUserTests(TestCase):

# class ChoiceModelTests(TestCase):
#     def test_minus_votes(self):
#         #question 생성
#         #choice votes 음수로 생성
#         time = timezone.now()
#         question = Question(pub_date=time)
#         minus_votes_choice = Choice(question, choice_text="minus votes choice", votes=-100)
#         self.assertIs(minus_votes_choice.is_minus_votes(), False)
#
#     def test_not_having_question(self):
#         # 질문이 없는 선택지 생성 테스트
#         no_question_choice = Choice(None, choice_text="No Question Choice.", votes=0)
#         self.assertIs(no_question_choice.has_question(), False)
#
# def create_choice(question, choice_text, votes):
#     return Choice.objects.create(question=question, choice_text=choice_text, votes=votes)