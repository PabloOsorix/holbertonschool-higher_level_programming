#!/usr/bin/python3


import unittest
from models.base import Base


class Test_BaseClass(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test__nb_objects(self):
        """Can't print nb_objects private
        class atributte"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_id(self):
        b0 = Base(2)
        self.assertEqual(b0.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base(54)
        self.assertEqual(b2.id, 54)
        b3 = Base(60)
        self.assertEqual(b3.id, 60)
        b1 = Base()
        self.assertEqual(b1.id, 4)

    def test_id_string(self):
        """Checks string like a 
        parameter to id"""
        b4 = Base("Holberton")
        self.assertEqual(b4.id, "Holberton")

    def test_floal_id(self):
        """Check floaat like id
        parameter"""
        b5 = Base(3.0)
        self.assertEqual(b5.id, 3.0)

    def test_list_id(self):
        """Pass list like args"""
        b_list = Base([4,5])
        self.assertEqual(b_list.id, [4,5])

    def test_tuple_id(self):
        """Pass tuple like arg"""
        b_tuple = Base((4, 5))
        self.assertEqual(b_tuple.id, (4, 5))

    def test_same_id(self):
        """Pass same id to different obj"""
        b_6 = Base(100)
        b_7 = Base(100)
        self.assertEqual(b_6.id, 100)
        self.assertEqual(b_7.id, 100)

    def test_id_set(self):
        """Pass set to arg"""
        b_8 = Base({2, 65})
        self.assertEqual(b_8.id, {2, 65})

    def test_id_inf(self):
        """Pass inf like id"""
        b_9 = Base(float('inf'))
        self.assertEqual(b_9.id, float('inf'))

    def test_Base_like_id(self):
        """Pass Base like id"""
        b_10 = Base(Base)
        self.assertEqual(b_10.id, Base)

    def test_dict_id(self):
        b_11 = Base({"5": 34})
        self.assertEqual(b_11.id, {"5": 34})

    def test_setfr_id(self):
        """Pass frozenset like arg id"""
        b_12 = Base(frozenset({23, 43, 54}))
        self.assertEqual(b_12.id, frozenset({23, 43, 54}))

    def test_none_id(self):
        """Pass None like id"""
        b_13 = Base(None)
        self.assertEqual(b_13.id, 9)

    



    def  test_to_mucho_args(self):
        """Too much arguments for Base class"""
        with self.assertRaises(TypeError):
            b_14 = Base(98, 98, ["2"])

    def test_same_object(self):
        """Same id but not same obj"""
        b_15 = Base(2)
        b_16 = Base(2)
        self.assertIsNot(b_15, b_16)

    def test_multiple_id(self):
        """Pass two arguments"""
        with self.assertRaises(TypeError):
            b_17 = Base(98, 99)

    def test_id_nan(self):
        """Pass NaN like arg"""
        b_18 = Base(float('nan'))
        self.assertNotEqual(b_18.id, float('nan'))
    
    def test_Base_like_id(self):
        """Pass Base like id (Recursion)"""
        b_20 = Base(Base)
        self.assertNotEqual(b_20.id, Base(2))






    """Tests static method to_json_string"""
    def test_to_json_string(self):
        """pass list with tuples to json string"""
        b_21 = Base.to_json_string([(5, 4, 6), (7, 8, 9)])
        self.assertEqual(b_21, '[[5, 4, 6], [7, 8, 9]]')

    def test_json_list_tuple(self):
        """pass list inside a tupe to json_string"""
        b_22 = Base.to_json_string(([2, 3, 4], [5, 4, 6]))
        self.assertEqual(b_22, '[[2, 3, 4], [5, 4, 6]]')

    def test_json_list_dict(self):
        """pass list with list and dict to json_string"""
        b_23 = Base.to_json_string([(4, 5, 6), {"5": "2", "6": "3"}])
        self.assertEqual(b_23, '[[4, 5, 6], {"5": "2", "6": "3"}]')

    def test_json_tuples_list(self):
        """pass tuple to json_string"""
        b_24= Base.to_json_string(([3, 4, 5], [6, 7, 8], [9, 10]))
        self.assertEqual(b_24, '[[3, 4, 5], [6, 7, 8], [9, 10]]')

    def test_json_int(self):        
        """Pass an integer"""
        b_25 = Base.to_json_string(129342)
        self.assertEqual(b_25, '129342')

    def test_json_tuple_list(self):
        """pass a tuple with lists"""
        b_26 = Base.to_json_string(([3, 4, 5], [6, 7, 8], [9, 10]))
        self.assertEqual(b_26,  '[[3, 4, 5], [6, 7, 8], [9, 10]]')

    def test_json_tuple_dict(self):        
        """pass list with tuple and dict"""
        b_27 = Base.to_json_string([(4, 5, 6), {"5": "2", "6": "3"}])
        self.assertEqual(b_27, '[[4, 5, 6], {"5": "2", "6": "3"}]')

    def test_json_dict(self):        
        """Pass a dict"""
        b_28 = Base.to_json_string({"2": 4, "4": 8, "8": 16})
        self.assertEqual(b_28, '{"2": 4, "4": 8, "8": 16}')

    def test_json_inf(self):        
        """Pass inf"""
        b_29 = Base.to_json_string(float('inf'))
        self.assertEqual(b_29, 'Infinity')

    def test_to_json_empty_list(self):        
        """Pass an empty list"""
        b_30 = Base.to_json_string([])
        self.assertEqual(b_30, [])

    def test_to_json_multiple_list(self):        
        """Pass multiple lists"""
        b_31 = Base.to_json_string([[[[[[[[]]]]]]]])
        self.assertEqual(b_31, '[[[[[[[[]]]]]]]]')

    def test_to_json_string(self):
        """Pass a string"""
        b_32 = Base.to_json_string("Hello Holberdummys")
        self.assertEqual(b_32, '"Hello Holberdummys"')

    def test_json_nan(self):
        b_33 = Base.to_json_string(float('nan'))
        self.assertEqual(b_33, 'NaN')

    """AssertRaises"""
    def test_to_joint_string_exceptions(self):
        """Pass methods and classes"""
        with self.assertRaises(TypeError):
            b_34 = Base.to_json_string(type(float(9)))

    def test_to_json_cls(self):
        """Pass a class Base"""
        with self.assertRaises(TypeError):
            b_35 = Base.to_json_string(Base(98))

    def test_to_json_multiple_parameter(self):        
        """Pass multiple parameter"""
        with self.assertRaises(TypeError):
            b_36 = Base.to_json_string({2, 3, 4, 5}, 'Hello')

    
    def test_json_frozenset(self):
        """Pass frozentset like arg"""
        with self.assertRaises(TypeError):
            b_37 = Base.to_json_string(frozenset({2, 3, 4, 5, 6, 7}))

    
    def test_json_set(self):
        """Pass set like arg"""
        with self.assertRaises(TypeError):
            b_38 = Base.to_json_string(({2, 3, 4, 5, 6, 7}))





    def test_no_arg(self):
        b_39 = Base()
        b_40 = Base()
        self.assertEqual(b_39.id, b_40.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    
    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))


    def test_to_json_string_none(self):
        self.assertEqual([], Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
