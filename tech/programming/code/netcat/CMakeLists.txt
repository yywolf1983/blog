cmake_minimum_required (VERSION 3.18)

project (netcat)

SET (CMAKE_BUILD_TYPE "Debug")
set (nc_VERSION "v072")

configure_file (
  "${PROJECT_SOURCE_DIR}/netcat-0.7.1/ncConfig.h.in"
  "${PROJECT_BINARY_DIR}/ncConfig.h"
  )

aux_source_directory(./netcat-0.7.1/src/ DIR_SRCS)
aux_source_directory(./netcat-0.7.1/lib/contrib/ DIR_GRTOPT)
add_executable(nc ${DIR_SRCS} ${DIR_GRTOPT})

include_directories("${PROJECT_BINARY_DIR}")

install (TARGETS nc DESTINATION bin)
