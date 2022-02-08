#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base

"""module to test class Rectangle"""


class Test_RectangleClass(unittest.TestCase):

    def test_id(self):
            """Test valid id"""
            r1 = Rectangle(10, 2)
            self.assertEqual(r1.id, 22)

    def test_ids(self):
        """Test valid ids"""
        r2 = Rectangle(32, 2)
        self.assertEqual(r2.id, 23)
        r3 = Rectangle(7, 2)
        self.assertEqual(r3.id, 24)
        r4 = Rectangle(32, 3, 0, 0, 77)
        self.assertEqual(r4.id, 77)

    def test_valid_parametrs(self):
        """Test with valid params"""
        r5 = Rectangle(3, 5, 2, 8, 108)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [3, 5, 2, 8, 108])
        r6 = Rectangle(43, 23)
        self.assertEqual([r6.width, r6.height], [43, 23])

    def test_params_defaults(self):
        """Tests default values for x, y"""
        r7 = Rectangle(32, 12)
        self.assertEqual([r7.x, r7.y], [0, 0])

    def test_params_defaults_2(self):
        """Tests default params"""
        r8 = Rectangle(32, 32, 13)
        self.assertEqual([r8.width, r8.height, r8.x, r8.y, r8.id],
                             [32, 32, 13, 0, 26])

    def test_params_setters(self):
        """Check all setters"""
        r9 = Rectangle(32, 34)
        r9.width = 21
        self.assertEqual(r9.width, 21)
        r9.height = 87
        self.assertEqual(r9.height, 87)
        r9.x = 55
        self.assertEqual(r9.x, 55)
        r9.y = 444
        self.assertEqual(r9.y, 444)

    def test_params_exceptions_args(self):
        """Checks wrong number of arguments, zero"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_params_exceptions_args_one(self):
        """Checks wrong number of arguments, 1 args"""
        with self.assertRaises(TypeError):
            r = Rectangle(21)

    def test_params_exceptions_args_six(self):
        """Checks wrong number of arguments, six"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 23, 12, 234, 4)

    def test_args_value_zero(self):
        """Check valid value"""
        msg = " must be > 0"
        err = ValueError
        try:
            Rectangle(-10, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, -10)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            Rectangle(0, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, 0)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        msg = " must be >= 0"
        try:
            Rectangle(10, 10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            Rectangle(10, 10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_rectangle_value(self):
        """Test Rectangle"""
        with self.assertRaises(ValueError):
            Rectangle(32, 0)

    def test_params_str_width(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle("string", 32)

    def test_params_str_height(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, "string")

    def test_params_str_x(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, "string")

    def test_params_str_y(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, "string")

    def test_params_str_width_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle("string", 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_str_x_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, "s")
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_str_y_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, 3, "s")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_list_width(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle([21], 32)

    def test_params_list_height(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, [32])

    def test_params_list_x(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, [1])

    def test_params_list_y(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, [43])

    def test_params_list_width_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle([234], 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_list_height_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(12, ["String"])
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_list_x_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_list_y_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_tuple_width(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle((21, 32), 32)

    def test_params_tuple_height(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, (32, 443))

    def test_params_tuple_x(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, (1, 54))

    def test_params_tuple_y(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, (43, 24))

    def test_params_tuple_width_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle((234, 32), 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_tuple_height_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(12, ("String", 32))
        except TypeError as e:
            self.assertEqual(str(e), 'height must be an integer')

    def test_params_tuple_x_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, ("s", 4))
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_tuple_y_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ("s", 542))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_dict_width(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21: 32}, 32)

    def test_params_dict_height(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32: 443})

    def test_params_dict_x(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1: 54})

    def test_params_dict_y(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43: 24})

    def test_params_dict_width_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle({234: 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_dict_height_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(12, {"String": 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_dict_x_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, {"s": 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_dict_y_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_none_width(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(None, 32)

    def test_params_none_height(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, None)

    def test_params_none_x(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, None)

    def test_params_dict_none(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, None)

    def test_params_none_width_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(None, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_none_height_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(12, None)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_none_x_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, None)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_none_y_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, 3, None)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_set_width(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21, 32}, 32)

    def test_params_set_height(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32, 443})

    def test_params_set_x(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1, 54})

    def test_params_set_y(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43, 24})

    def test_params_set_width_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle({234, 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_set_height_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(12, {"String", 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_set_x_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, {"s", 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_set_y_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_func_width(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(len, 32)

    def test_params_func_height(self):
        """Check func as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, len)

    def test_params_func_x(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, len)

    def test_params_func_y(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, len)

    def test_params_func_width_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(len, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_func_height_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(12, len)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_func_x_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, len)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_func_y_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, 3, len)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_area(self):
        """Simple area test"""
        r = Rectangle(32, 2)
        self.assertEqual(r.area(), 64)

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            s1 = Rectangle(10, 5)
            s1.area(32343)

    def test_00_case_width_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.width, 5)

    def test_00_case_height_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.height, 10)

    def test_00_case_x_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.x, 0)

    def test_00_case_y_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.y, 0)

    def test_00_case_id_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.id, 2)

    def test_00_case_width_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.width, 8)

    def test_00_case_height_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.height, 12)

    def test_00_case_x_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.x, 5)

    def test_00_case_y_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.y, 3)

    def test_00_case_id_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.id, 26)

    def test_19_case_whitout_values(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_20_case_whit_just_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_21_case_whit_more_than_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 7, 8, 9, 10)

    def test_22_case_whit_float_values(self):
        with self.assertRaises(TypeError):
            Rectangle(3.8, 5.6, 7, 9)

    def test_23_case_whit_list(self):
        with self.assertRaises(TypeError):
            Rectangle([7, 9], 3)

    def test_24_case_check_area_result(self):
        new_obj = Rectangle(3, 2)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area()
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(3, 5, 6)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(float('inf'), 5)

    def test_dimensions(self):
        """ check if w & h dimensions are validate """
        rDim = Rectangle(2, 8)
        self.assertEqual(rDim.width, 2)
        self.assertEqual(rDim.height, 8)
        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)
        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)
        self.assertRaises(TypeError, Rectangle, 'Cinco', 10)
        self.assertRaises(TypeError, Rectangle, 10, '5')
        self.assertRaises(TypeError, Rectangle, None, 10)
        self.assertRaises(TypeError, Rectangle, 10, None)
        self.assertRaises(TypeError, Rectangle, True, 10)
        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 5, -10)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """
        rUpdateArg = Rectangle(1, 2)
        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)
        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 2)
        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.x, 10)
        rUpdateArg.update(10, 10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update('A', 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 'A')
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        self.assertRaises(TypeError, rUpdateArg.update(), 6, "3", 10, 19, 14)
        self.assertRaises(TypeError, rUpdateArg.update(), 10, 5, 5, None, 0)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """
        rUpdateKarg = Rectangle(1, 2)
        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)
        rUpdateKarg.update(id=10, width=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 2)
        rUpdateKarg.update(id=10, width=7, height=8)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        rUpdateKarg.update(id=10, width=7, height=8, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        self.assertEqual(rUpdateKarg.x, 9)
        rUpdateKarg.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 30)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)
  
    def test_03_create_rectangle_success(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Rectangle)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, list"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = [32, 43]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_set(self):
        """Check valid types, set"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {32, 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = (32, 43)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {"Hi": 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, float"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 3.14
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_none(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = None
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, list"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = [32, 43]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_set(self):
        """Check valid types, set"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {32, 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = (32, 43)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {"Hi": 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, float"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 3.14
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_none(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = None
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)


    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)


    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])



    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))


    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))


    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
