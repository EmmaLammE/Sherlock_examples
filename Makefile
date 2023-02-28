# CXX=g++ -m64
# CXXFLAGS=-Iobjs/ -O3 -std=c++11 -Wall -fPIC

# APP_NAME=simple_add
# OBJDIR=objs

# default: $(APP_NAME)

# .PHONY: dirs clean

# dirs:
#                 /bin/mkdir -p $(OBJDIR)/

# clean:
#                 /bin/rm -rf $(OBJDIR) *.ppm *~ $(APP_NAME)

# OBJS=$(OBJDIR)/main.o

# $(APP_NAME): dirs $(OBJS)
#                 $(CXX) $(CXXFLAGS) -o $@ $(OBJS) -lm -lpthread

# $(OBJDIR)/%.o: %.cpp
#                 $(CXX) $< $(CXXFLAGS) -c -o $@

# $(OBJDIR)/%.o: $(COMMONDIR)/%.cpp
#         $(CXX) $< $(CXXFLAGS) -c -o $@

# # $(OBJDIR)/main.o: $(COMMONDIR)/CycleTimer.h

CXX = g++ -m64
CXXFLAGS = -std=c++11 -Wall -fPIC -pedantic-errors -g

SRCS = main.cpp 
OBJDIR=objs
OBJS=$(OBJDIR)/main.o
# OBJS = main.o #${SRCS:.cpp=.o}
# HEADERS = aaaa.h

MAIN = myprog

.PHONY: dirs clean

all: ${MAIN}
	@echo   Simple compilter named myprog has been compiled

dirs:
	/bin/mkdir -p $(OBJDIR)/

${MAIN}: dirs $(OBJS) #${HEADERS}
	${CXX} ${CXXFLAGS} -o $@ $(OBJS)

$(OBJDIR)/%.o: %.cpp
	$(CXX) $< $(CXXFLAGS) -c -o $@

# clean:
# 	${RM} ${PROGS} ${OBJS} *.o *~
clean:
	/bin/rm -rf $(OBJDIR) *.ppm *~ $(MAIN)
