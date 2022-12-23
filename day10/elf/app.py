from queue import LifoQueue
from typing import Type, List

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
    #with open('testinput-large.txt') as f:
        lines = f.readlines()

    strength = SignalStrength([20, 60, 100, 140, 180, 220])

    for line in lines:
        commands = line.strip().split()
        strength.process_commands(commands)

    total_strength = 0
    for key,val in strength.special_cycles_result.items():
        total_strength += val
        #print(f'cycle {key} : {val}')
        
    print(f'Total: {total_strength}')
    print()
    
    for index, crt in enumerate(strength.crt_output):
        print(crt, sep= None, end= "")
        if (index+1) % 40 == 0:
             print()
    
class SignalStrength:
    
    def __init__(self, special_cycles: List[int]) -> None:
        self.register_val = 1
        self.cycle_cnt = 0
        self.special_cycles = special_cycles
        self.special_cycles_result: dict[str, int] = {}
        self.crt_output: List[str] = []
        
    def process_commands(self, commands) -> None:
        if commands[0] == "noop":
            self.process_command(commands[0])
        else:
            self.process_command(commands[0], int(commands[1]))
        
    def process_command(self, cmd: str, value:int = 0):
        #print(f'Current cycle: {self.cycle_cnt}')
        if cmd == "noop":
            self.evaluate_crt()
            
            self.cycle_cnt += 1
            self.handle_special_cycles()
        elif cmd == "addx":
            self.evaluate_crt()
            self.cycle_cnt += 1
            self.handle_special_cycles()

            self.evaluate_crt()
            self.cycle_cnt += 1
            self.handle_special_cycles()
            self.register_val += value

        else:
            print(f'No command: {cmd} + {value}')
                    
    def evaluate_crt(self) -> None:
        # if register is +- 1 of cycle_cnt then set #, otherwise .
        if(self.cycle_cnt % 40 in [self.register_val - 1, self.register_val, self.register_val + 1]):
            self.crt_output.append('#')
        else:
            #print (f'nothing for {self.cycle_cnt} and {self.register_val}')
            self.crt_output.append('.')
                    
    def handle_special_cycles(self) -> None:
        if self.cycle_cnt in self.special_cycles:
            print(f'storing {self.cycle_cnt} for val {self.register_val}')
            self.special_cycles_result[self.cycle_cnt] = self.cycle_cnt * self.register_val
        
    def __str__(self): 
        return "implement this"
    
    def __repr__(self):
        return self.__str__()
        