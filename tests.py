#! /usr/bin/env python3

import unittest

import scraper

class ScraperUnitTest(unittest.TestCase):

    def setUp(self):
        self.recipe_url = 'http://www.bonappetit.com/recipe/salt-and-pepper-rib-eye'
        self.scraped_content = scraper.scrape(self.recipe_url)

    def test_title(self):
        self.assertEqual(self.scraped_content['title'], 'Salt-and-Pepper Rib Eye')

    def test_url(self):
        self.assertEqual(self.scraped_content['url'], self.recipe_url)

    def test_img_url(self):
        self.assertEqual(self.scraped_content['img_url'],
                         'http://www.bonappetit.com/wp-content/uploads/2010/06/salt-and-pepper-rib-eye-940x600.jpg')

    def test_ingredients(self):
        self.assertIn('1 1½"-2" bone-in rib eye (about 2 pounds)',
                      self.scraped_content['ingredients'])
        self.assertIn('2 teaspoon kosher salt, divided',
                      self.scraped_content['ingredients'])
        self.assertIn('1 teaspoon coarsely ground black pepper',
                      self.scraped_content['ingredients'])

    def test_directions(self):
        self.assertIn(self.scraped_content['directions'], 'Put steak on a wire rack')
        self.assertIn(self.scraped_content['directions'], 'Build a two-zone fire')
        self.assertIn(self.scraped_content['directions'], 'season with corase sea salt, and serve')


    def test_servings(self):
        self.assertEqual(self.scraped_content['servings'], '')

    def test_time(self):
        self.assertEqual(self.scraped_content['total_time'], '')
        self.assertEqual(self.scraped_content['cooking_time'], '')


if __name__ == '__main__':
    unittest.main()
