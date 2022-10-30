from tortoise.contrib.test import TestCase

from database.memo import Memo


class TestDB(TestCase):
    async def test_all_은_모든_레코드를_가져온다(self) -> None:
        # Given
        await Memo.create(title="test 제목", body="test 본문")
        await Memo.create(title="test 제목2", body="test 본문2")

        # When
        memos = await Memo.all()

        # Then
        self.assertEqual(len(memos), 2)
        self.assertEqual(memos[0].title, "test 제목")
        self.assertEqual(memos[0].body, "test 본문")
        self.assertEqual(memos[1].title, "test 제목2")
        self.assertEqual(memos[1].body, "test 본문2")
