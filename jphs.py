import os, pwd, sys, pexpect

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))

class jphs:

	def jphideit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry5")
		self.spass = self.password.get_text()
		self.fchooser = self.builder.get_object("filechooserbutton1")
		self.hidefile = self.fchooser.get_filename()
		if self.sfile != '' and self.password != '' and self.hidefile != None:
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/jphide'
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			self.outfile = outdir + '/' +tail
			if os.path.isfile(self.outfile):
				os.remove(self.outfile)
			child = pexpect.spawn(execdir + '/programs/jphide.sh', [self.sfile, self.outfile, self.hidefile, execdir])
			child.expect('Passphrase:', timeout=2)
			child.sendline(self.spass)
			child.expect('Re-enter  :', timeout=2)
			child.sendline(self.spass)
			child.expect(pexpect.EOF)
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()

	def jpseekit2(self, widget):
		self.file = self.builder.get_object("entry1")
		self.sfile = self.file.get_text()
		self.password = self.builder.get_object("entry4")
		self.spass = self.password.get_text()
		if self.sfile != '' and self.spass != '':
			head, tail = os.path.split(self.sfile)
			outdir = home + tail + '/jpseek'
			if not os.path.isdir(outdir):
				os.mkdir(outdir)
			self.outfile = outdir + '/' + tail + '.txt'
			if os.path.isfile(self.outfile):
				os.remove(self.outfile)
			child = pexpect.spawn(execdir + '/programs/jpseek.sh', [self.sfile, self.outfile, execdir])
			child.expect('Passphrase:', timeout=2)
			child.sendline(self.spass)
			child.expect(pexpect.EOF)
		else:
			def hidedialog(widget):
				self.nofiledialog.hide()
			self.nofiledialog = self.builder.get_object("dialog1")
			self.nofiledialogbutton = self.builder.get_object("button5")
			self.nofiledialogbutton.connect("clicked",hidedialog)
			self.nofiledialog.show()