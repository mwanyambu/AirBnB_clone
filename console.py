#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self):
        """empty line"""
        pass

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_EOF(self, arg):
        """exit program upon end of file"""
        return True

    def do_create(self, arg):
        """new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            base_instance = eval(arg)()
            base_instance.save()
            print(base_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """display the string representation"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if len(args) < 2:
                print("** instance id missing **")
                return
            class_name= args[0]
            obj_id = args[1]
            obj_key = class_name + "." + obj_id
            objects = models.storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """delete a specific instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if len(args) < 2:
                print("** instance id missing **")
                return
            class_name = args[0]
            obj_id = args[1]
            obj_key = lass_name + "." + obj_id
            objects = models.storage.all()
            if obj_key in objects:
                del objects[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """display all instances"""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = eval(arg)
                print([str(obj) for obj in objects.values() if type(obj) == class_name])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """update an isntance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if len(args) < 2:
                print ("** instance id missing **")
                return
            class_name = args[0]
            obj_id =  args[1]
            obj_key = class_name + "." + obj_id
            objects = models.storage.all()
            if obj_key in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                attribute_name = args[2]
                value = args[3]
                if hasattr(objects[obj_key], attribute_name):
                    typeval = type(getattr(objects[obj_key], attribute_name))
                    value = typeval(value)
                    setattr(objects[obj_key], attribute_name, value)
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
