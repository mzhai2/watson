import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.selected = set()
        self.count = 0
        tk.Label(self, text='Generator Part 1').pack()
        self.choice_textvariable = tk.StringVar()
        self.choice_textvariable.set('Dropdown')
        choiceMenuButton = tk.Menubutton(self, textvariable=self.choice_textvariable, indicatoron=True, borderwidth=1, relief="raised")
        choiceMenu = tk.Menu(choiceMenuButton, tearoff=False)

        self.choices = {}
        for choice in ('Voltage', 'Calcium', 'CalciumER'):
            self.choices[choice] = tk.IntVar(value=0)
            choiceMenu.add_checkbutton(label=choice, variable=self.choices[choice], 
                                 onvalue=1, offvalue=0, command=self.update_choice_str)
        choiceMenuButton.configure(menu=choiceMenu)
        choiceMenuButton.pack(padx=10, pady=10)
        
        countFrame = tk.Frame(self)
        countFrame.pack(padx=10, pady=10)
        tk.Label(countFrame, text='how many BRANCHTYPE (1-7)').pack(side = tk.LEFT)
        self.count_input = tk.StringVar()
        tk.Entry(countFrame, textvariable=self.count_input).pack(side = tk.LEFT)
        self.count_input.set("1")

        bottomframe = tk.Frame(self)
        bottomframe.pack(side = tk.BOTTOM)
        button = tk.Button(bottomframe, text="Generate", command=self.generate)
        button.pack(pady=10, side = tk.BOTTOM)
    
    def writeCptParams(self):
        with open('CptParams.par', 'w') as f:
            f.write('COMPARTMENT_VARIABLE_TARGETS {}\nBRANCHTYPE\n'.format(self.count))
            for i in range(self.count):
                f.write('{} {}\n'.format(i+1, ' '.join(list(self.selected))))

    def changeFrame(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text='Generator Part 2').pack()
        
        self.channelName = tk.StringVar()        
        channelNameFrame = tk.Frame(self)
        channelNameFrame.pack(padx=10, pady=10)
        tk.Label(channelNameFrame, text='ChannelName').pack(side = tk.LEFT)
        tk.Entry(channelNameFrame, textvariable=self.channelName).pack(side = tk.LEFT)

        inputFrame = tk.Frame(self)
        inputFrame.pack(padx=10, pady=10)
        tk.Label(inputFrame, text='Input').pack(side = tk.LEFT)
        self.input_textvariable = tk.StringVar()
        self.input_textvariable.set('Dropdown')
        inputMenuButton = tk.Menubutton(inputFrame, textvariable=self.input_textvariable, indicatoron=True, borderwidth=1, relief="raised")
        inputMenu = tk.Menu(inputMenuButton, tearoff=False)

        self.inputs = {}
        for input_ in self.selected:
            self.inputs[input_] = tk.IntVar(value=0)
            inputMenu.add_checkbutton(label=input_, variable=self.inputs[input_], onvalue=1, offvalue=0, command=self.update_input_str)
        inputMenuButton.configure(menu=inputMenu)
        inputMenuButton.pack(padx=10, pady=10, side = tk.LEFT)

        outputFrame = tk.Frame(self)
        outputFrame.pack(padx=10, pady=10)
        tk.Label(outputFrame, text='Output').pack(side = tk.LEFT)
        self.output_textvariable = tk.StringVar()
        self.output_textvariable.set('Dropdown')
        outputMenuButton = tk.Menubutton(outputFrame, textvariable=self.output_textvariable, indicatoron=True, borderwidth=1, relief="raised")
        outputMenu = tk.Menu(outputMenuButton, tearoff=False)
        self.outputs = {}
        for output_ in self.selected:
            self.outputs[output_] = tk.IntVar(value=0)
            outputMenu.add_checkbutton(label=output_, variable=self.outputs[output_], onvalue=1, offvalue=0, command=self.update_output_str)
        outputMenuButton.configure(menu=outputMenu)
        outputMenuButton.pack(padx=10, pady=10, side = tk.LEFT)

        channelTypeFrame = tk.Frame(self)
        channelTypeFrame.pack(padx=10, pady=10)
        tk.Label(channelTypeFrame, text='ChannelType').pack(side = tk.LEFT)
        self.channel_textvariable = tk.StringVar()
        self.channel_textvariable.set('Dropdown')
        channelTypeMenuButton = tk.Menubutton(channelTypeFrame, textvariable=self.channel_textvariable, indicatoron=True, borderwidth=1, relief="raised")
        channelTypeMenu = tk.Menu(channelTypeMenuButton, tearoff=False)
        self.channelTypes = {}
        for channelType_ in list(range(1,8)):
            self.channelTypes[channelType_] = tk.IntVar(value=0)
            channelTypeMenu.add_checkbutton(label=channelType_, variable=self.channelTypes[channelType_], onvalue=1, offvalue=0, command=self.update_channel_str)
        channelTypeMenuButton.configure(menu=channelTypeMenu)
        channelTypeMenuButton.pack(padx=10, pady=10, side = tk.LEFT)
        bottomframe = tk.Frame(self)
        bottomframe.pack(side = tk.BOTTOM)
        button = tk.Button(bottomframe, text="Add", command=self.add)
        button.pack(pady=10, side = tk.BOTTOM)

    def update_choice_str(self):
        choices = []
        for name, var in self.choices.items():
            if var.get() == 1:
                choices.append(name)
        self.choice_textvariable.set(' '.join(choices))

    def update_output_str(self):
        outputs = []
        for name, var in self.outputs.items():
            if var.get() == 1:
                outputs.append(name)
        self.output_textvariable.set(' '.join(outputs))

    def update_input_str(self):
        inputs = []
        for name, var in self.inputs.items():
            if var.get() == 1:
                inputs.append(name)
        self.input_textvariable.set(' '.join(inputs))

    def update_channel_str(self):
        channels = []
        for name, var in self.channelTypes.items():
            if var.get() == 1:
                channels.append(name)
        self.channel_textvariable.set(' '.join(map(str, sorted(channels))))


    def generate(self):
        for name, var in self.choices.items():
            if var.get() == 1:
                self.selected.add(name)

        if len(self.selected) > 0:
            try:
                self.count = int(self.count_input.get())
                if self.count < 1 or self.count > 7:
                    print('entry {} is out of range of 1-7'.format(self.count))
                else:
                    self.writeCptParams()
                    self.changeFrame()
            except ValueError:
                print('entry is not an integer')
        else:
            print('must select at least one option')

    def add(self):
        channels = []
        for name, var in self.channelTypes.items():
            if var.get() == 1:
                channels.append(name)
        if len(channels) == 0:
            print('Warning: no channels')

        outputs = []
        for name, var in self.outputs.items():
            if var.get() == 1:
                outputs.append(name)

        if len(outputs) == 0:
            print('Warning: no outputs')

        inputs = []
        for name, var in self.inputs.items():
            if var.get() == 1:
                inputs.append(name)
        
        if len(inputs) == 0:
            print('Warning: no inputs')

        channel_name = self.channelName.get()
        if len(channel_name) == 0:
            print('Warning: no channel name')

        
        with open('ChanParams.par', 'w') as f:
            f.write('CHANNEL_TARGETS {}\nBRANCHTYPE\n'.format(len(channels)))
            for channel in channels:    
                f.write('{} {} [{}] [{}]\n'.format(channel, channel_name, ' '.join(inputs), ' '.join(outputs)))

if __name__ == "__main__":
    root = tk.Tk()
    GUI(root).pack(fill="both", expand=True)
    root.mainloop()
    