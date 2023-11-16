import main
import unittest
# import os


class TestMyApp(unittest.TestCase):
    def test_myTest(self):
        app = main.FoodApp()
        print(app)
        self.assertIsNotNone(app)

    def test_GIU(self):
        app = main.FoodApp()
        gui = app.build()
        print(gui)
        self.assertIsNotNone(gui)

    def test_widgets(self):
        app = main.FoodApp()
        gui = app.build()
        widgets = gui.children
        self.assertIsNotNone(widgets)
        self.assertEqual(len(widgets), 2)

        for i in widgets:
            self.assertIsNotNone(i)

    # testing assets
    # def test_assets(self):
    #     cwd = os.getcwd()
    #    img1 =  os.path.join(cwd, "folder", "filename.xxx" )
    #     os.path.isfile(img1)
    #   self.assertEqual(os.path.isfile(img1), True)


if __name__ == '__main__':
    unittest.main()
