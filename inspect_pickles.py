import pickle
import numpy as np
import matplotlib.pyplot as plt


def process_hh4b_pickle(namepicklefile):
	with open(namepicklefile, 'rb') as pkfl:
		pickled_obj = pickle.load(pkfl)

	if not type(pickled_obj) == type(dict()):
		raise ValueError('Expected dictionary from file: {}'.format(
			namepicklefile)+\
		'instead got: {}'.format(type(pickled_obj)))

	pickle_dict = pickled_obj
	start_times = []
	end_times = []
	processes = []
	statuses = []
	for key, val in pickle_dict.items():
		print('\n')
		print('key: {}'.format(key))


		if type(val) == type(dict()):
			processes.append(str(key))
			print()
			for subkey, subval in val.items():
				print('	{}: {}'.format(subkey, subval))

			try:
				start_times.append(val['start_time'])
				end_times.append(val['end_time'])
				statuses.append(val['status'])
			except KeyError as ke:
				print('cant find status, start or end times: {}'.format(ke))
				start_times.append(np.nan)
				end_times.append(np.nan)
		else:
			print('value type: {}'.format(type(val)))
			print('value: {}'.format(val))


	min_start = np.min(start_times)
	start_times = np.array(start_times) - min_start
	end_times = np.array(end_times) - min_start
	width = end_times - start_times

	return processes, width, start_times

def process_stmc_pickle(namepicklefile):
	with open(namepicklefile, 'rb') as pkfl:
		pickled_obj = pickle.load(pkfl)

	if not type(pickled_obj) == type(dict()):
		raise ValueError('Expected dictionary from file: {}'.format(
			namepicklefile)+\
		'instead got: {}'.format(type(pickled_obj)))

	pickle_dict = pickled_obj
	start_times = []
	end_times = []
	processes = []
	statuses = []
	for key, val in pickle_dict.items():
		print('\n')
		print('key: {}'.format(key))


		if type(val) == type(dict()):
			processes.append(str(key))
			print()
			for subkey, subval in val.items():
				print('	{}: {}'.format(subkey, subval))

			try:
				start_times.append(val['start_time'])
				end_times.append(val['end_time'])
			except KeyError as ke:
				print('cant find status, start or end times: {}'.format(ke))
				start_times.append(np.nan)
				end_times.append(np.nan)
		else:
			print('value type: {}'.format(type(val)))
			print('value: {}'.format(val))


	min_start = np.min(start_times)
	start_times = np.array(start_times) - min_start
	end_times = np.array(end_times) - min_start
	width = end_times - start_times

	return processes, width, start_times

## HH4B 4 Processes 4 cores ===================================================
# picklefilename = 'background-dijet_bkgd_dict_original.pickle'

# with open(picklefilename, 'rb') as pkfl:
# 	pickled_obj = pickle.load(pkfl)

# if not type(pickled_obj) == type(dict()):
# 	raise ValueError('Expected dictionary from file: {}'.format(
# 		picklefilename)+\
# 	'instead got: {}'.format(type(pickled_obj)))

# pickle_dict = pickled_obj
# start_times = []
# end_times = []
# processes = []
# statuses = []
# for key, val in pickle_dict.items():
# 	print('\n')
# 	print('key: {}'.format(key))
# 	processes.append(str(key))
# 	if type(val) == type(dict()):
# 		print()
# 		for subkey, subval in val.items():
# 			print('	{}: {}'.format(subkey, subval))
# 	else:
# 		print('value type: {}'.format(type(val)))
# 		print('value: {}'.format(val))
# 	try:
# 		start_times.append(val['start_time'])
# 		end_times.append(val['end_time'])
# 		statuses.append(val['status'])
# 	except KeyError as ke:
# 		print('cant find status, start or end times: {}'.format(ke))
# 		start_times.append(np.nan)
# 		end_times.append(np.nan)


# nanmask = np.isnan(start_times)
# min_start = np.min(start_times)
# start_times = np.array(start_times) - min_start
# end_times = np.array(end_times) - min_start
# width = end_times - start_times


# plt.barh(processes, width, left=start_times)
# plt.ylabel('Process Number', fontsize=12)
# plt.xlabel('Time (s)', fontsize=12)
# plt.title('Dijet Samples Processing Time', fontsize=12)
# plt.savefig('Plots/hh4b_processing_orig.png')
# plt.show()
#==============================================================================


## HH4B 4 Processes 4 cores ===================================================
# picklefilename_1 = 'background-dijet_bkgd_multiprocess-4_dict.pickle'
# with open(picklefilename_1, 'rb') as pkfl:
# 	pickled_obj = pickle.load(pkfl)

# if not type(pickled_obj) == type(dict()):
# 	raise ValueError('Expected dictionary from file: {}'.format(
# 		picklefilename)+\
# 	'instead got: {}'.format(type(pickled_obj)))

# pickle_dict = pickled_obj
# start_times = []
# end_times = []
# processes = []
# statuses = []
# for key, val in pickle_dict.items():
# 	print('\n')
# 	print('key: {}'.format(key))


# 	if type(val) == type(dict()):
# 		processes.append(str(key))
# 		print()
# 		for subkey, subval in val.items():
# 			print('	{}: {}'.format(subkey, subval))

# 		try:
# 			start_times.append(val['start_time'])
# 			end_times.append(val['end_time'])
# 			statuses.append(val['status'])
# 		except KeyError as ke:
# 			print('cant find status, start or end times: {}'.format(ke))
# 			start_times.append(np.nan)
# 			end_times.append(np.nan)
# 	else:
# 		print('value type: {}'.format(type(val)))
# 		print('value: {}'.format(val))



# nanmask = np.isnan(start_times)
# min_start = np.min(start_times)
# start_times = np.array(start_times) - min_start
# end_times = np.array(end_times) - min_start
# width = end_times - start_times


# plt.barh(processes, width, left=start_times)
# plt.ylabel('Process Number', fontsize=12)
# plt.xlabel('Time (s)', fontsize=12)
# plt.title('Dijet Samples Processing Time', fontsize=12)
# plt.savefig('Plots/hh4b_processing_4cores.png')
# plt.show()
#==============================================================================


## STMC  =================================================== 
processes, width, start_times = process_stmc_pickle(
	'forloop-1_file-0-to-15_dict.pickle')
	

plt.barh(processes, width, left=start_times)
plt.ylabel('Process Number', fontsize=12)
plt.xlabel('Time (s)', fontsize=12)
plt.title('Charged Pion Sample STMC Processing Time', fontsize=12)
plt.savefig('Plots/ml4p_processing_forloop.png')
plt.show()
#==============================================================================


## STMC  =================================================== 
processes, width, start_times = process_stmc_pickle(
	'multiprocess-15_file-0-to-15_dict.pickle')
	

plt.barh(processes, width, left=start_times)
plt.ylabel('Process Number', fontsize=12)
plt.xlabel('Time (s)', fontsize=12)
plt.title('Charged Pion Sample STMC Processing Time', fontsize=12)
plt.savefig('Plots/ml4p_multiprocess-15_file-0-to-15.png')
plt.show()
#==============================================================================


## STMC  =================================================== 
processes, width, start_times = process_stmc_pickle(
	'multiprocess-5_file-0-to-5_dict.pickle')
	

plt.barh(processes, width, left=start_times)
plt.ylabel('Process Number', fontsize=12)
plt.xlabel('Time (s)', fontsize=12)
plt.title('Charged Pion Sample STMC Processing Time', fontsize=12)
plt.savefig('Plots/ml4p_multiprocess-5_file-0-to-5.png')
plt.show()
#==============================================================================


## STMC  =================================================== 
processes, width, start_times = process_stmc_pickle(
	'multiprocess-6_file-0-to-15_dict.pickle')
	

plt.barh(processes, width, left=start_times)
plt.ylabel('Process Number', fontsize=12)
plt.xlabel('Time (s)', fontsize=12)
plt.title('Charged Pion Sample STMC Processing Time', fontsize=12)
plt.savefig('Plots/ml4p_multiprocess-6_file-0-to-15.png')
plt.show()
#==============================================================================


## STMC  =================================================== 
processes, width, start_times = process_stmc_pickle(
	'multithread-5_file-0-to-5_dict.pickle')
	

plt.barh(processes, width, left=start_times)
plt.ylabel('Process Number', fontsize=12)
plt.xlabel('Time (s)', fontsize=12)
plt.title('Charged Pion Sample STMC Processing Time', fontsize=12)
plt.savefig('Plots/ml4p_multithread-5_file-0-to-5.png')
plt.show()
#==============================================================================


