from llvmlite import ir

#Holds functions, global variables, and metadata.
module = ir.Module(name = "my_module")

func_type = ir.FunctionType(ir.VoidType(), []) #LLVM requires code to live inside functions. Even if your language doesn’t use functions (yet), you need a dummy function (like main) to hold instructions.
func = ir.Function(module, func_type, name="main")


block = func.append_basic_block(name="entry") #'indent' block inside the function
builder = ir.IRBuilder(block)#the builder allows code to be added to the block

#adding global vars for test
a_var = ir.GlobalVariable(module, ir.IntType(32), "a")
a_var.initializer = ir.Constant(ir.IntType(32), 5)

#Return void (required for LLVM functions)
builder.ret_void()

# Step 6: Print the generated IR
print(module)