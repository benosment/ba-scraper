#! /usr/bin/env python3

import unittest

import scraper

class ScraperUnitTest(unittest.TestCase):

    def setUp(self):
        self.ribeye_url = 'http://www.bonappetit.com/recipe/salt-and-pepper-rib-eye'
        self.cauliflower_url = 'http://www.bonappetit.com/recipe/roasted-cauliflower-with-lemon-parsley-dressing'
        self.ribeye_scrape = scraper.scrape(self.ribeye_url)
        self.cauliflower_scrape = scraper.scrape(self.cauliflower_url)

    def test_title(self):
        self.assertEqual(self.ribeye_scrape['title'], 'Salt-and-Pepper Rib Eye')
        self.assertEqual(self.cauliflower_scrape['title'], 'Roasted Cauliflower with Lemon-Parsley Dressing')

    def test_url(self):
        self.assertEqual(self.ribeye_scrape['url'], self.ribeye_url)
        self.assertEqual(self.cauliflower_scrape['url'], self.cauliflower_url)

    def test_img_url(self):
        self.assertEqual(self.ribeye_scrape['img_url'],
                         'http://www.bonappetit.com/wp-content/uploads/2010/06/salt-and-pepper-rib-eye-940x600.jpg')
        self.assertEqual(self.cauliflower_scrape['img_url'],
                         'http://www.bonappetit.com/wp-content/uploads/2013/10/roasted-cauliflower-with-lemon-parsley-dressing-940x560.jpg')

    def test_ingredients(self):
        self.assertIn('1 1½"-2" bone-in rib eye (about 2 pounds)',
                      self.ribeye_scrape['ingredients'])
        self.assertIn('2 teaspoon kosher salt, divided',
                      self.ribeye_scrape['ingredients'])
        self.assertIn('1 teaspoon coarsely ground black pepper',
                      self.ribeye_scrape['ingredients'])
        self.assertIn('1 head cauliflower (about 2 lb.), cut into florets, including tender leaves',
                      self.cauliflower_scrape['ingredients'])
        self.assertIn('1 cup fresh flat-leaf parsley leaves',
                      self.cauliflower_scrape['ingredients'])
        self.assertIn('1/2 teaspoon finely grated lemon zest',
                      self.cauliflower_scrape['ingredients'])

    def test_directions(self):
        self.assertIn('Put steak on a wire rack',
                      ' '.join(self.ribeye_scrape['directions']))
        self.assertIn('Build a two-zone fire',
                      ' '.join(self.ribeye_scrape['directions']))
        self.assertIn('season with coarse sea salt, and serve',
                      ' '.join(self.ribeye_scrape['directions']))
        self.assertIn('Preheat oven to 425°. Toss cauliflower',
                      ' '.join(self.cauliflower_scrape['directions']))
        self.assertIn('Meanwhile, pulse parsley, lemon juice,',
                      ' '.join(self.cauliflower_scrape['directions']))
        self.assertIn('Lemon-parsley mixture can be made 4 hours ahead. Cover and chill.',
                      ' '.join(self.cauliflower_scrape['directions']))


    def test_servings(self):
        self.assertEqual(self.ribeye_scrape['servings'], '')
        self.assertEqual(self.cauliflower_scrape['servings'], '4')

    def test_time(self):
        self.assertEqual(self.ribeye_scrape['total_time'], '')
        self.assertEqual(self.ribeye_scrape['cooking_time'], '')
        self.assertEqual(self.cauliflower_scrape['total_time'], '35 min')
        self.assertEqual(self.cauliflower_scrape['cooking_time'], '35 min')


if __name__ == '__main__':
    unittest.main()
